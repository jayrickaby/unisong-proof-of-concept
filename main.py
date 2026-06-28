import sqlite3
from config import *
from local import *
from musicbrainz import *
from poc.Album import Album

def initialise():
    initialiseEnvironment()
    initialiseMusicBrainz()
    initialiseDatabase()

def main():
    initialise()
    #
    # searchForAlbums(input("Look for files: "))
    # createAlbumsFromFiles()
    #
    # albums = getLocalAlbums()
    #
    # getIdFromAlbum(albums['Atom Heart Mother (2011 Remaster)'])


    # albums = []
    # albumsData = searchAlbum(input("Please enter album name: "), 5)
    # for albumData in albumsData['release-group-list']:
    #     album = Album(albumData)
    #     print(f"{album.title} by {album.artists}")
    #     addAlbum(album)

if __name__ == '__main__':
    main()