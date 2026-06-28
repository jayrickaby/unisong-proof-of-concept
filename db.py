import sqlite3

CENTRAL_DB = "unisong.db"
# LOCAL_DB = "local.db" ... for later

def createUnisongAlbumTable():
    db = sqlite3.connect(CENTRAL_DB)
    q = """
        CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY,
            releaseGroupMBID TEXT NOT NULL,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            year INTEGER NOT NULL,
            description TEXT NOT NULL
            ); 
        """
    db.execute(q)
    db.close()

def

def addAlbum(newAlbum):
    db = sqlite3.connect(CENTRAL_DB)
    cursor = db.cursor()

    q = """
        INSERT INTO albums (releaseGroupMBID, title, artist, year, description) VALUES (?, ?, ?, ?, ?);
    """

    cursor.execute(q,(newAlbum.releaseGroupMBID, newAlbum.title, newAlbum.artists[0], newAlbum.year, ""))
    db.commit()
    cursor.close()
