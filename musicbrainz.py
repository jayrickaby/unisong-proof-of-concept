import musicbrainzngs

def searchAlbum(query, limit):
    return musicbrainzngs.search_release_groups(query=query, limit=limit, type='album')