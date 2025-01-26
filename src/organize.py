from mutagen.mp4 import MP4
import os
from Book import Book

def read_m4b_metadata(file_path):
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
            file_list.append(os.path.join(root, file))
    
    return file_list

def filter_files_by_type(files, extensions):
    return [file for file in files if any(file.endswith(ext) for ext in extensions)]


def organize(dir, title_style):
    files = list_all_files(dir)

    # only filter for m4b files for now
    filtered_files = filter_files_by_type(files, ['m4b'])

    for file in filtered_files:
        book1 = Book(read_m4b_metadata(file), title_style)
        print(book1)