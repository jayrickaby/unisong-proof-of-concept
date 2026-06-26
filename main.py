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

def searchAlbum(query, limit):
    return musicbrainzngs.search_release_groups(query=query, limit=limit, type='album')

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


    albums = searchAlbum(input("Please enter album name: "), 5)
    for album in albums['release-group-list']:
        print(f"{album['title']} by {album['artist-credit']}")


if __name__ == '__main__':
    main()