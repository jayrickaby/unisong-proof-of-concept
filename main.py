import sqlite3
from config import *
from local import *
from poc.Album import Album

def initialise():
    print("Initialising...")
    initialiseEnvironment()
    initialiseMusicBrainz()
    initialiseDatabase()

def main():
    initialise()
    processLocalEntities(input("Look for files: "))

if __name__ == '__main__':
    main()