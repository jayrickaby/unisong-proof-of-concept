class LocalRelease:
    def __init__(self):
        # Raw db stuff
        self.releaseMBID = ""

        # Extras
        self.title = ""
        self.artists = []
        self.year = ""
        self.disambiguation = ""
        self.releaseGroupMBID = ""

        # path to access localtrack dict
        self.tracks = []

    def parseLocalTrack(self, track):
        splitAlbum = track.release.split('(', 1)
        splitAlbum[1] = splitAlbum[1].split(')')[0]

        self.title = splitAlbum[0].strip()
        self.disambiguation = splitAlbum[1].strip()
        self.artists = track.artists
        self.year = track.year