
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
    def __init__(self, data, title_style):
        self.title_style = title_style

        self.author = get_specific_metadata(data, metadata_tags['artist'])
        self.album = get_specific_metadata(data, metadata_tags['album'])
        self.title = get_specific_metadata(data, metadata_tags['title'])

    def __repr__(self):
        return f"'{self.title}' by {self.author}, part of {self.album}"

    def get_path(self):
        print('building path', self)
        



# author > album > title > file