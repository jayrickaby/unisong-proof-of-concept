import os

import mutagen
import glob

EXTENSIONS = ["**/*.flac", "**/*.wav", "**/*.mp3"]

files = []

def searchForAlbums(path):
    for extension in EXTENSIONS:
        foundFiles = glob.glob(extension, root_dir=path, recursive=True)

        for file in foundFiles:
            files.append(os.path.join(path, file))

    print(files)
