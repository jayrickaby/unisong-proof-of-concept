class Album:
    def __init__(self):
        self.title = ""
        self.artists = []
        self.year = 0
        self.description = ""

    def parseLocalTrack(self, data):
        if data["album"][0]:
            self.title = data["album"][0]

        if data["artist"]:
            self.artists = data["artist"]

        if data["date"]:
            self.year = data["date"]

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
