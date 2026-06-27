import os

import mutagen
import glob

from poc.Album import Album

EXTENSIONS = ["**/*.flac", "**/*.wav", "**/*.mp3"]

albums = {}
files = []

def searchForAlbums(path):
    for extension in EXTENSIONS:
        foundFiles = glob.glob(extension, root_dir=path, recursive=True)

        for file in foundFiles:
            files.append(os.path.join(path, file))

def createAlbumsFromFiles():
    for file in files:
        data = mutagen.File(file)

        album = Album()
        album.parseLocalTrack(data)

        if album.title not in albums and album.title != "":
            print(f"Found: '{album.title}'")
            albums[album.title] = album

def getLocalAlbums():
    return albums
