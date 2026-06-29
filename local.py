import glob
import os

from musicbrainz import *
from poc.Album import *
from poc.LocalRelease import *
from poc.LocalTrack import *

EXTENSIONS = ["**/*.flac", "**/*.wav", "**/*.mp3"]

albums = {}

def processLocalEntities(path):
    localTracks = searchForLocalTracks(path)

    if localTracks is None or localTracks == {}:
        return

    localReleases = {}

    for track in localTracks:
        localRelease = extrapolateLocalRelease(track)

        if localRelease.fullTitle in localReleases:
            localReleases[localRelease.fullTitle]
            continue



    lookupLocalReleasesMBID()
    extrapolateAlbums()



# find tracks, get metadata and store into a LocalTrack
def searchForLocalTracks(path):
    absolutePath = os.path.abspath(path)
    absolutePath = absolutePath.strip()

    print(f"Looking for files in: {absolutePath}")

    foundFiles = []

    for extension in EXTENSIONS:
        foundFiles.extend(glob.glob(extension, root_dir=absolutePath, recursive=True))

    # early return if no files found
    if len(foundFiles) == 0:
        print("No files found!")
        return None

    tracks = {}

    for file in foundFiles:
        # needed for mutagen extraction
        fullPath = os.path.join(absolutePath, file)
        print("Found: " + file)

        track = LocalTrack()
        track.parseLocalTrack(fullPath)

        tracks[fullPath] = track

    return tracks

# from Local tracks, create releases
def extrapolateLocalRelease(track: LocalTrack):
    print(f"Extrapolating from {track.path}")

    localRelease = {}

    # early return to avoid null or duplicates/overrides
    if track.release == "":
        return

    # Avoid duplicate releases
    if track.release in localReleases:
        print(f"Adding {track.path} to existing {track.release}")
        localReleases[track.release].tracks.append(track.path)
        return

    localRelease = LocalRelease()
    localRelease.parseLocalTrack(track)
    print(f"Creating {localRelease.title}")
    localReleases[track.release] = localRelease

    print(f"Adding {track.path} to new {track.release}")
    localReleases[track.release].tracks.append(track.path)

def lookupLocalReleasesMBID():
    for release in localReleases:
        localData = localReleases[release]
        mbData = getReleaseDataFromLocalRelease(localData)

        localReleases[release].releaseMBID = mbData['id']
        localReleases[release].releaseGroupMBID = mbData['release-group']['id']

def extrapolateAlbums():
    for release in localReleases:
        releaseData = localReleases[release]

        albumData = getAlbumDataFromLocalRelease(releaseData)

        album = Album()
        album.parseMusicBrainzData(albumData)
        album.addLocalRelease(release)

        if not albums[album.title]:
            albums[album.title] = album

