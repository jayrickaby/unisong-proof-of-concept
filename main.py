from venv import create

from dotenv import load_dotenv
import os
import sqlite3

# For this proof-of-concept, we will use a few third party libraries in order to perform API requests.
# For the actual programming project, API requests will all be done in-house.
import musicbrainzngs

from poc.Album import Album

def initialise():
    # Load before others to properly initialise env variables
    print("Initialising environment variables...")
    load_dotenv()
    musicBrainzUsername = os.getenv("MUSICBRAINZ_USERNAME")
    musicBrainzPassword = os.getenv("MUSICBRAINZ_PASSWORD")

    print("Setting MusicBrainz useragent...")
    musicbrainzngs.set_useragent("proof of concept application", "0.0.0", contact="jayrickaby@pm.me")
    print("Authorising MusicBrainz credentials...")
    musicbrainzngs.auth(musicBrainzUsername, musicBrainzPassword)

    print("Creating database tables...")
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