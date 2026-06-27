import sqlite3
from config import *
from db import *
from poc.Album import Album

def initialise():
    initialiseEnvironment()
    initialiseMusicBrainz()

    createAlbumTable()

def searchAlbum(query, limit):
    return musicbrainzngs.search_release_groups(query=query, limit=limit, type='album')

def createAlbumTable():
    db = sqlite3.connect("unisong.db")
    cursor = db.cursor()
    q = """
        CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            year INT NOT NULL,
            description STRING NOT NULL
            ); 
        """
    cursor.execute(q)
    cursor.close()

def addAlbum(newAlbum):
    db = sqlite3.connect("unisong.db")
    cursor = db.cursor()

    q = f"""
        INSERT INTO albums (title, artist, year, description) VALUES (?, ?, ?, ?)
    """

    cursor.execute(q, (newAlbum.title, newAlbum.artists[0], 0, "the best"))
    db.commit()
    cursor.close()


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