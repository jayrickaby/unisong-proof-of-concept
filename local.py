import mutagen
import glob

EXTENSIONS = ["*.flac", "*.wav", "*.mp3"]

def searchForAlbums(path):
    files = []
    for extension in EXTENSIONS:
        files.extend(glob.glob(f"{path}/{extension}"))

    print(files)
