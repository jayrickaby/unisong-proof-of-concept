from venv import create

from dotenv import load_dotenv
import os
import sqlite3

# For this proof-of-concept, we will use a few third party libraries in order to perform API requests.
# For the actual programming project, API requests will all be done in-house.
import musicbrainzngs

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

def searchArtist(query, limit):
    return musicbrainzngs.search_artists(query=query, limit=limit)

def main():
    initialise()
    unisongDatabase = sqlite3.connect("unisong.db")
    unisongCursor = unisongDatabase.cursor()
    createAlbumTableQuery = """
    CREATE TABLE IF NOT EXISTS albums (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        artist TEXT NOT NULL,
        year INT NOT NULL,
        description STRING NOT NULL
        );
    """

    print("Creating Albums table...")
    unisongCursor.execute(createAlbumTableQuery)
    unisongCursor.close()


    artists = searchArtist(input("Please enter artist name: "), 5)
    for artist in artists['artist-list']:
        print(f"{artist['name']} - {artist['type']} from {artist['area']['name']}.")


if __name__ == '__main__':
    main()
