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
    