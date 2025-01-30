import os
import shutil

metadata_tags = {
    "title": "\xa9nam",
    "artist": "\xa9ART",
    "album": "\xa9alb",
    "track": "\xa9trk"
}

def get_specific_metadata(metadata, tag_name):
    if metadata and tag_name in metadata:
        return metadata[tag_name][0]
    else:
        print("Tag not found or no metadata available")
        return None

class Book:
    def __init__(self, name, path, data):
        self.name = name
        self.path = path

        self.author = get_specific_metadata(data, metadata_tags['artist'])
        self.album = get_specific_metadata(data, metadata_tags['album'])
        self.title = get_specific_metadata(data, metadata_tags['title'])

    def __repr__(self):
        return f"'{self.title}' by {self.author}, part of {self.album} | {self.name}"

    # dry run
    def get_path(self):
        return f"{self.author} > {self.album} > {self.title} > {self.name}"
    
    def move_file(self, dir):
        # build path
        relative_destination_file_path = os.path.join(self.author, self.album, self.title)
        absolute_destination_path = os.path.join(dir, relative_destination_file_path)
        os.makedirs(absolute_destination_path)

        # destination_file = os.path.join(path, os.path.basename(path))
        shutil.move(self.path, absolute_destination_path)
        print('successfully moved:', self.name)



# author > album > title > file