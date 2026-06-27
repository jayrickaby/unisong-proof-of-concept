import sqlite3
from config import *
from db import *
from musicbrainz import *
from poc.Album import Album

def initialise():
    initialiseEnvironment()
    initialiseMusicBrainz()

    createAlbumTable()

def main():
    initialise()

    albums = []
    albumsData = searchAlbum(input("Please enter album name: "), 5)
    for albumData in albumsData['release-group-list']:
        album = Album(albumData)
        print(f"{album.title} by {album.artists}")
        addAlbum(album)

if __name__ == '__main__':
    main()