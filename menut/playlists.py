import json
import consolemenu as cm
import consolemenu.items as cmi
from customMenuRows import BlankItem

import db
from objects import Playlist, Song, User
from menut.albums import createAlbum, createPlaylist, editPlaylist

def playPlaylist(playlist, song):
        i = playlist.songs.index(song)
        songs = [ {'name': song.name, 'artist': song.artist, 'path': song.path} for song in playlist.songs[i:] ]
        with open("playlist", 'w') as fout:
            json.dump(songs, fout)
        playlist.songs[i].play()

def buildPlaylistMenu(user:User, kind):
    if kind == 'p':
        menuTitle = "Playlists"
        table = "userplaylist"
    
    elif kind == 'a':
        menuTitle = "Album"
        table = "album"

    else:
        input("Kind not found :/")
        return

    albumMenuTop = cm.ConsoleMenu(f"{menuTitle}", f"Select the number to open the {menuTitle.lower()}")
    albums = db.interact(f'SELECT playlistid, title FROM {table} WHERE creator = \'{user.name}\';')
    if len(albums) == 0:
        albumMenuTop.append_item(cmi.MenuItem(f"No {menuTitle.lower()}s found"))
    for aid, album in albums:
        albumItem = cm.ConsoleMenu(album)
        a = Playlist(aid, album, [Song(*song) for song in db.interact(f'SELECT songid, title, createdby, filelocation, explicit FROM song NATURAL JOIN {table}songs WHERE playlistid = \'{aid}\'')])
        for song in a.songs:
            albumItem.append_item(cmi.FunctionItem(song.name, playPlaylist, [a, song], menu=albumItem))
        albumItem.append_item(BlankItem(""))  
        albumMenuTop.append_item(cmi.SubmenuItem(album, albumItem, albumMenuTop))

    albumMenuTop.append_item(BlankItem(""))
    if kind == 'p':
        albumMenuTop.append_item(cmi.FunctionItem(f"Create {menuTitle}", createPlaylist, [user], should_exit=True))
        albumMenuTop.append_item(cmi.FunctionItem(f"Edit {menuTitle}", editPlaylist, [user], should_exit=True))
    elif kind == 'a':
        albumMenuTop.append_item(cmi.FunctionItem(f"Create {menuTitle}", createAlbum, [user], should_exit=True))
    albumMenuTop.show()
