class LocalTrack:
    def __init__(self):
        # Required db fields
        self.trackMBID = ""
        self.path = ""

        # Extra stuff to help album / release cataloging
        self.title = ""
        self.artists = []
        self.release = ""
        self.year = ""
        self.release = ""

    def parseLocalTrack(self, data):
        # use .get() as it returns 'None' if invalid
        if data.get("title"):
            self.title = data["title"][0]

        if data.get("album"):
            self.release = data["album"][0]

        if data.get("artist"):
            self.artists = data["artist"][0]

        if data.get("year"):
            self.year = data["year"][0]

    def setPath(self, path):
        self.path = path

    def setMBID(self, trackMBID):
        self.trackMBID = trackMBID