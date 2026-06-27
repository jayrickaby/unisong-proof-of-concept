import os
from dotenv import load_dotenv

# For this proof-of-concept, we will use a few third party libraries in order to perform API requests.
# For the actual programming project, API requests will all be done in-house.
import musicbrainzngs

def initialiseEnvironment():
    load_dotenv()

def initialiseMusicBrainz():
    musicbrainzngs.set_useragent(
        "proof of concept application",
        "0.0.0",
        contact="jayrickaby@pm.me"
    )

    musicbrainzngs.auth(
        os.getenv("MUSICBRAINZ_USERNAME"),
        os.getenv("MUSICBRAINZ_PASSWORD")
    )