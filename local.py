import mutagen
import glob

EXTENSIONS = ["*.flac", "*.wav", "*.mp3"]

def searchForAlbums(path):
    files = []
    for extension in EXTENSIONS:
        files.extend(glob.glob(extension, root_dir=path))

    print(files)
