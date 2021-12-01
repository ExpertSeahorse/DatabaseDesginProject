import subprocess
import json

import db
class User:
    def __init__(self, username, firstName, lastName, dob, country, kind, followers, following, playlists) -> None:
        self.name = username
        self.firstName = firstName
        self.lastName = lastName
        self.dob = dob
        self.country = country
        self.kind = kind
        self.followers = followers
        self.following = following
        # Get the list of Songs from the title of the playlist
        if playlists != None:
            self.playlists = []
            for id, title in playlists:
                # Cast the song rows into Song objects
                songs = [Song(*song) for song in db.interact(f'SELECT songid, title, createdby, filelocation, explicit FROM song NATURAL JOIN userplaylistsongs WHERE playlistid = \'{id}\'')]
                self.playlists.append(Playlist(id, title, songs))

class Playlist:
    def __init__(self, pid:int, name:str, songs:list):
        self.pid = pid
        self.name = name
        self.songs = songs

class Song:
    def __init__(self, sid:int, name:str, artist:str=None, path:str=None, explicit:bool=None) -> None:
        self.id = sid
        self.name = name
        self.artist = artist
        self.explicit = explicit
        self.path = path

    def play(self):
        subprocess.Popen(f" start /wait python .\MusicPlayer.py {self.name} {self.path}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def match(self, query):
        return query.lower() in self.name.lower() or query.lower() in self.artist.lower()

    def __str__(self) -> str:
        return json.dumps(vars(self))
    

# songs = [
#     Song("Satisfaction", "The Rolling Stones", datetime.date(1965, 5, 1)), 
#     Song("Imagine", "John Lennon", datetime.date(1971, 10, 1)), 
#     Song("What's Going On", "Marvin Gaye", datetime.date(1971, 2, 1)),
#     Song("Respect", "Aretha Franklin", datetime.date(1967, 4, 1)),
#     Song("Good Vibrations", "The Beach Boys", datetime.date(1966, 10, 1)),
#     Song("Johnny B. Goode", "Chuck Berry", datetime.date(1958, 4, 1)),
#     Song("Hey Jude", "The Beatles", datetime.date(1968, 8, 1)),
#     Song("Smells Like Teen Spirit", "Nirvana", datetime.date(1991, 9, 1)),
#     Song("What'd I Say", "Ray Charles", datetime.date(1959, 6, 1))
# ]
# """
# We will eventually replace these with DB calls. Until then these help with designing the interface
# """
# import datetime
# class User:
#     def __init__(self, usern, passw, firstName, lastName, email, dob, country, following, followed_by, userType, playlistType, artistName, verified, favSongs, favArtists) -> None:
#         self.usern = usern
#         self.passw = passw
#         self.firstName = firstName
#         self.lastName = lastName
#         self.email = email
#         self.dob = dob
#         self.country = country
#         self.following = following
#         self.followed_by = followed_by

#         # not Guest
#         self.userType = userType
#         self.playlistType = playlistType

#         # Artist specific
#         self.artistName = artistName
#         self.verified = verified

#         # Premium specific
#         self.favSongs = favSongs
#         self.favArtists = favArtists

# userGuest = User(
#     "guest",
#     "pass",
#     "Guest",
#     "User",
#     "guest@test.com",
#     datetime.datetime.now(),
#     "Argentina",
#     ["James", "Adam"],
#     ["Adam", "Jules"],
#     "guest",
#     "", "", False, [], []
# )

# userPrem = User(
#     "premium",
#     "pass",
#     "Premium",
#     "User",
#     "premium@test.com",
#     datetime.datetime.now(),
#     "Egypt",
#     ["Mike"],
#     ["Adam", "George"],
#     "premium",
#     "playlist", "", False, ["Uptown Funk", "I Gotta Feeling"], ["Bruno Mars", "The Black Eyed Peas"]
# )

# userArtist = User(
#     "artist",
#     "pass",
#     "Artist",
#     "User",
#     "artist@test.com",
#     datetime.datetime.now(),
#     "United Kingdom",
#     [],
#     ["Otto", "Allison Downs", "Lily-Anne"],
#     "artist",
#     "album", "myArtistName", True, [], []
# )
