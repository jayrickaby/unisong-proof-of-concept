import glob
import mutagen
import os

from musicbrainz import *
from poc.LocalAlbum import LocalRelease
from poc.LocalTrack import LocalTrack

EXTENSIONS = ["**/*.flac", "**/*.wav", "**/*.mp3"]

localReleases = {}
localTracks = {}

def processLocalEntities(path):
    searchForLocalTracks(path)
    extrapolateLocalReleases()

def searchForLocalTracks(path):
    for extension in EXTENSIONS:
        foundFiles = glob.glob(extension, root_dir=path, recursive=True)

        # early return if no files found
        if len(foundFiles) < 0:
            return

        for file in foundFiles:
            # needed for mutagen extraction
            fullPath = os.path.join(path, file)

            data = mutagen.File(fullPath)

            track = LocalTrack()
            track.parseLocalTrack(data)
            track.setPath(fullPath)

            localTracks[fullPath] = track

def extrapolateLocalReleases():
    for path in localTracks:
        # early return to avoid null or duplicates/overrides
        track = localTracks[path]

        if track.release == "":
            return

        if track.release in localReleases:
            localReleases[track.release].tracks.append(path)

        localRelease = LocalRelease()
        localRelease.parseLocalTrack(track)

        localReleases[track.release] = localRelease









