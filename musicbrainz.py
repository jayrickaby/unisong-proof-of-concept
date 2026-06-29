import musicbrainzngs
from poc.LocalRelease import LocalRelease

DEFAULT_LIMIT = 1

def getReleaseDataFromLocalRelease(release: LocalRelease):
    # TODO: Surely theres a better way to do this?
    if len(release.artists) == 0 or release.year is None:
        result = musicbrainzngs.search_releases(
            query=release.title,
            comment=release.disambiguation,
            limit=DEFAULT_LIMIT, type='album')
    else:
        result = musicbrainzngs.search_releases(
            query=release.title,
            comment=release.disambiguation,
            artistname=release.artists[0],
            date=release.year,
            limit=DEFAULT_LIMIT, type='album')

    return result['release-list'][0]

def getAlbumDataFromLocalRelease(release: LocalRelease):
    return musicbrainzngs.get_release_group_by_id(release.releaseGroupMBID, includes=["artists"])['release-group']

