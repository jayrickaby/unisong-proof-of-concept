import os
import importlib.metadata
from dotenv import load_dotenv

# For this proof-of-concept, we will use a few third party libraries in order to perform API requests.
# For the actual programming project, API requests will all be done in-house.
import musicbrainzngs

NAME = ("unisong-proof-of-concept")
VERSION = importlib.metadata.version(NAME)
CONTACT = importlib.metadata.metadata(NAME).get("Author-email", "jayrickaby@pm.me")

def initialiseEnvironment():
    # don't want people using my credentials
    load_dotenv()

def initialiseMusicBrainz():
    musicbrainzngs.set_useragent(
        NAME,
        VERSION,
        contact=CONTACT
    )

    musicbrainzngs.auth(
        os.getenv("MUSICBRAINZ_USERNAME"),
        os.getenv("MUSICBRAINZ_PASSWORD")
    )