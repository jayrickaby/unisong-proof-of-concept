import mutagen
import glob

EXTENSIONS = ["**/*.flac", "**/*.wav", "**/*.mp3"]

files = []

def searchForAlbums(path):
    files = []
    for extension in EXTENSIONS:
        files.extend(glob.glob(extension, root_dir=path, recursive=True))

    print(files)
