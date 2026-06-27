import sqlite3

CENTRAL_DB = "unisong.db"
# LOCAL_DB = "local.db" ... for later

def createAlbumTable():
    db = sqlite3.connect(CENTRAL_DB)
    q = """
        CREATE TABLE IF NOT EXISTS albums (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            year INTEGER NOT NULL,
            description TEXT NOT NULL
            ); 
        """
    db.execute(q)
    db.close()

def addAlbum(newAlbum):
    db = sqlite3.connect(CENTRAL_DB)
    cursor = db.cursor()

    q = """
        INSERT INTO albums (title, artist, year, description) VALUES (?, ?, ?, ?);
    """

    cursor.execute(q,
                   (newAlbum.title, newAlbum.artists[0], 0, "")
                   )
    db.commit()
    cursor.close()
