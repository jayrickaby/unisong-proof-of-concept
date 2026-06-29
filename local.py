import glob
import os

from musicbrainz import *
from poc.LocalRelease import LocalRelease
from poc.LocalTrack import LocalTrack

EXTENSIONS = ["**/*.flac", "**/*.wav", "**/*.mp3"]

localReleases = {}
localTracks = {}

def processLocalEntities(path):
    searchForLocalTracks(path)
    extrapolateLocalReleases()
    lookupLocalReleasesMBID()

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
        return

    for file in foundFiles:
        # needed for mutagen extraction
        fullPath = os.path.join(absolutePath, file)
        print("Found: " + file)

        track = LocalTrack()
        track.parseLocalTrack(fullPath)

        localTracks[fullPath] = track

# from Local tracks, create releases
def extrapolateLocalReleases():
    for path in localTracks:
        print(f"Extrapolating from {path}")

        track = localTracks[path]

        # early return to avoid null or duplicates/overrides
        if track.release == "":
            continue

        if track.release in localReleases:
            print(f"Adding {path} to existing {track.release}")
            localReleases[track.release].tracks.append(path)
            continue

        localRelease = LocalRelease()
        localRelease.parseLocalTrack(track)
        print(f"Creating {localRelease.title}")
        localReleases[track.release] = localRelease

        print(f"Adding {path} to new {track.release}")
        localReleases[track.release].tracks.append(path)

def lookupLocalReleasesMBID():
    for release in localReleases:
        releaseData = localReleases[release]
        mbid = getReleaseIdFromLocalRelease(releaseData)

        localReleases[release].releaseMBID = mbid



