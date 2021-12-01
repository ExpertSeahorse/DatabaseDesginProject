import json
import consolemenu as cm
import consolemenu.items as cmi

import db
from objects import Playlist, Song

def playPlaylist(playlist, song):
        i = playlist.songs.index(song)
        songs = [ {'name': song.name, 'artist': song.artist, 'path': song.path} for song in playlist.songs[i:] ]
        with open("playlist", 'w') as fout:
            json.dump(songs, fout)
        playlist.songs[i].play()

def buildPlaylistMenu(user, kind):
    if kind == 'p':
        playlistMenuTop = cm.ConsoleMenu("Playlists", "Select the number to open the playlist")
        for playlist in user.playlists:
            playlistItem = cm.ConsoleMenu(playlist.name)
            for song in playlist.songs:
                playlistItem.append_item(cmi.FunctionItem(song.name, playPlaylist, [playlist, song], menu=playlistItem)) 
            playlistMenuTop.append_item(cmi.SubmenuItem(playlist.name, playlistItem, playlistMenuTop))
        playlistMenuTop.show()

    elif kind == 'a':
        albumMenuTop = cm.ConsoleMenu("Albums", "Select the number to open the album")
        for aid, album in db.interact(f'SELECT playlistid, title FROM album WHERE creator = \'{user.name}\';'):
            albumItem = cm.ConsoleMenu(album)
            a = Playlist(aid, album, [Song(*song) for song in db.interact(f'SELECT songid, title, createdby, filelocation, explicit FROM song NATURAL JOIN albumsongs WHERE playlistid = \'{aid}\'')])
            for song in a.songs:
                albumItem.append_item(cmi.FunctionItem(song.name, playPlaylist, [a, song], menu=albumItem))
            albumMenuTop.append_item(cmi.SubmenuItem(album, albumItem, albumMenuTop))
        albumMenuTop.show()
