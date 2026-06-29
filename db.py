import sqlite3
from poc.Album import Album

CENTRAL_DB = "unisong.db"

def createUnisongAlbumTable():
    db = sqlite3.connect(CENTRAL_DB)
    q = """
        CREATE TABLE IF NOT EXISTS unisongAlbums (
            id INTEGER PRIMARY KEY,
            releaseGroupMBID TEXT NOT NULL,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            date TEXT NOT NULL,
            description TEXT NOT NULL
            ); 
        """
    db.execute(q)
    db.close()

def createUnisongReleasesTable():
    db = sqlite3.connect(CENTRAL_DB)
    q = """
        CREATE TABLE IF NOT EXISTS unisongReleases (
            id INTEGER PRIMARY KEY,
            releaseMBID TEXT NOT NULL,
            
            releaseGroupMBID TEXT NOT NULL,
            CONSTRAINT fk_ReleaseGroup
            FOREIGN KEY(releaseGroupMBID) 
            REFERENCES unisongAlbums(releaseGroupMBID),
            
            disambiguation TEXT
            ); 
        """
    db.execute(q)
    db.close()

def addUnisongAlbum(newAlbum: Album):
    db = sqlite3.connect(CENTRAL_DB)
    cursor = db.cursor()

    q = """
        INSERT INTO unisongAlbums (releaseGroupMBID, title, artist, date, description) VALUES (?, ?, ?, ?, ?);
    """

    cursor.execute(q,(newAlbum.releaseGroupMBID, newAlbum.title, newAlbum.artists[0], newAlbum.date, ""))
    db.commit()
    cursor.close()

def addUnisongRelease(unisongRelease):
    db = sqlite3.connect(CENTRAL_DB)
    cursor = db.cursor()

    q = """
        INSERT INTO unisongReleases (releaseMBID, releaseGroupMBID, disambiguation) VALUES (?, ?, ?);
    """

    cursor.execute(q,(unisongRelease.releaseMBID, unisongRelease.releaseGroupMBID, unisongRelease.disambiguation))
    db.commit()
    cursor.close()