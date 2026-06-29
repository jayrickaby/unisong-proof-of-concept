class Album:
    def __init__(self):
        self.releaseGroupMBID = ""
        self.title = ""
        self.artists = []
        self.date = None
        self.description = ""

        self.releases = [] # stores keys for localReleases

    def parseMusicBrainzData(self, data):
        self.releaseGroupMBID = data["id"]
        self.title = data["title"]
        self.date = data["first-release-date"]

        for artist in data["artist-credit"]:
            self.artists.append(artist['artist']['name'])

    def addLocalRelease(self, title: str):
        self.releases.append(title)
