class Album:
    def __init__(self):
        self.title = ""
        self.artists = []
        self.year = 0
        self.description = ""

    def parseLocalTrack(self, data):
        self.title = data["album"][0]
        self.artists = data["artist"]
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
