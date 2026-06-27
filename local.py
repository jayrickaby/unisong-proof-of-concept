import mutagen
import glob

EXTENSIONS = ["*.flac", "*.wav", "*.mp3"]

def searchForAlbums(path):
    files = []
    for extension in EXTENSIONS:
        files.append(glob.glob(f"{path}/{extension}"))

    print(files)
