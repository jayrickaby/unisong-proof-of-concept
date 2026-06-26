from dotenv import load_dotenv
import os

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

def main():
    initialise()
    test = musicbrainzngs.search_artists(query="King Crimson")
    print(test['artist-list'][0]['id'])
    print(test['artist-list'][0]['name'])

if __name__ == '__main__':
    main()
