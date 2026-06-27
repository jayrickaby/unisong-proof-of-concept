class Album:
    def __init__(self):
        self.title = ""
        self.artists = []
        self.year = 0
        self.description = ""

    def parseLocalTrack(self, data):
        # use .get() as it returns 'None' if invalid
        if data.get("album"):
            self.title = data["album"][0]

        if data.get("artist"):
            self.artists = data["artist"]

        if data.get("date"):
            self.year = data["date"][0]

    #     self.__parseData(data)
    #
    # # Relative to <release-group>
    # def __parseData(self, data):
    #     self.title = data['title']
    #
    #     for artist in data['artist-credit']:
    #         if isinstance(artist, dict):
    #             self.artists.append(artist['name'])
    #
