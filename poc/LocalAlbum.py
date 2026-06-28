class LocalRelease:
    def __init__(self):
        self.title = ""
        self.artists = []
        self.year = 0

    def parseLocalTrack(self, data):
        # use .get() as it returns 'None' if invalid
        if data.get("album"):
            self.title = data["album"][0]

        if data.get("artist"):
            self.artists = data["artist"]

        if data.get("date"):
            self.year = data["date"][0]
