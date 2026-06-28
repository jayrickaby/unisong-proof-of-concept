import musicbrainzngs

DEFAULT_LIMIT = 1

def searchAlbum(query, limit=DEFAULT_LIMIT):
    return musicbrainzngs.search_release_groups(query=query, limit=limit, type='album')

def getIdFromAlbum(album):
    # Assume all albums have a title, but may have a disambiguation
    pureTitle = album.title.split("(")[0]
    print("Looking for album with pure title: ", pureTitle)

    result = {}

    if album.artists:
        result = musicbrainzngs.search_release_groups(query=pureTitle, artistname=album.artists[0] ,limit=DEFAULT_LIMIT, type='album')

    else:
        result = musicbrainzngs.search_release_groups(query=pureTitle, limit=DEFAULT_LIMIT, type='album')

    data = result['release-group-list']

    if len(data) > 0:
        print("Found with id: " + data[0]['id'])
        return data[0]['id']

    return None