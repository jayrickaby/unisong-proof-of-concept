from pathlib import Path
from mutagen.easyid3 import EasyID3

class LocalTrack:
    def __init__(self):
        # Required db fields
        self.trackMBID = ""
        self.path = ""

        # Extra stuff to help album / release cataloging
        self.title = ""
        self.artists = []
        self.release = ""
        self.year = None
        self.release = ""

    def parseLocalTrack(self, path):
        print(path)

        data = EasyID3(path)

        print(data)

        try:
            self.title = data["title"][0]
        except KeyError:
            print("No title tag, using file name!")
            self.title = Path(path).stem

        try:
            self.release = data["album"][0]
        except KeyError:
            print("No album tag!")
            return                  # early return as whats the point

        try:
            self.artists = data["artist"][0]
        except KeyError:
            print("No artist tag!")

        try:
            self.year = data["date"][0]
        except KeyError:
            print("No year tag!")

        self.path = path

    def setMBID(self, trackMBID):
        self.trackMBID = trackMBID