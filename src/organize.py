from mutagen.mp4 import MP4
import os
from Book import Book

def read_audio_metadata(file_path):
    try:
        audio = MP4(file_path)
        return {key: audio.tags[key] for key in audio.tags.keys()}
    except Exception as e:
        print(f"Error reading metadata: {e}")
        return None

def list_all_files(directory):
    file_list = []

    for root, _, files in os.walk(directory):
        for file in files:
            name = os.path.basename(file)
            path = os.path.join(root, file)
            file_list.append({'name':name, 'path':path})
    
    return file_list

def filter_files_by_type(files, extensions):
    filtered_files = []
    for file in files:
        for ext in extensions:
            if file['name'].endswith(ext):
                filtered_files.append(file)
                break
    return filtered_files


def organize(dir, is_dry_run):
    files = list_all_files(dir)

    # only filter for m4b files for now
    filtered_files = filter_files_by_type(files, ['m4b'])

    for file in filtered_files:
        book = Book(file['name'], file['path'], read_audio_metadata(file['path']))
        if (is_dry_run):
            print(book.get_path())
        else:
            book.move_file(dir)