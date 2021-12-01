import consolemenu as cm
import consolemenu.items as cmi

import db
from objects import Song
from customMenuRows import BlankItem

def buildSearch():
    try:
        search = input("Search> ")
        found = []
        temp = (db.interact(f'SELECT songid, title, createdby, filelocation FROM song WHERE title LIKE \'%{search}%\';'))
        if len(temp) != 0:
            found.append(("song", temp.copy()))
            temp.clear()
        
        temp = (db.interact(f'SELECT displayname FROM artist WHERE displayname LIKE \'%{search}%\';'))
        if len(temp) != 0:
            found.append(("artist", temp.copy()))
            temp.clear()
        
        temp = (db.interact(f'SELECT playlistid, title, creator FROM album WHERE title LIKE \'%{search}%\';'))
        if len(temp) != 0:
            found.append(("album", temp.copy()))
            temp.clear()

        temp = (db.interact(f'SELECT playlistid, title, creator FROM playlist NATURAL JOIN userplaylist JOIN users ON(creator=username) WHERE title LIKE \'%{search}%\';'))
        if len(temp) != 0:
            found.append(("playlist", temp.copy()))
            temp.clear()

        temp = (db.interact(f'SELECT username FROM users WHERE username LIKE \'%{search}%\';'))
        if len(temp) != 0:
            found.append(("user", temp.copy()))
            temp.clear()

        if len(found) == 0:
            searchMenuTop = cm.ConsoleMenu("Search", f"{search}", prologue_text=f"{search} does not match any song or artist names")
            searchMenuTop.append_item(cmi.FunctionItem("Search Again", buildSearch, menu=searchMenuTop, should_exit=True))
            searchMenuTop.show()
        else:
            searchMenuTop = cm.ConsoleMenu("Search", f"{search}")
            for entry in found:
                # Display all song results
                if entry[0] == "song":
                    searchMenuTop.append_item(cmi.MenuItem("----- Songs -----"))
                    for song in entry[1]:
                        song = Song(*song)
                        searchMenuTop.append_item(cmi.FunctionItem(song.name+", "+song.artist, song.play)) 
                    searchMenuTop.append_item(BlankItem(""))

                # Display all artist results
                elif entry[0] == "artist":
                    searchMenuTop.append_item(cmi.MenuItem("----- Artists -----"))
                    for artist_display_name in [e.strip("'") for i in entry[1] for e in i]:
                        artistSubmenu = cm.ConsoleMenu(artist_display_name)
                        for aid, album in db.interact(f"SELECT playlistid, title FROM album JOIN artist ON creator=username WHERE displayname = '{artist_display_name}';"):
                            artistSubmenu.append_item(cmi.MenuItem(f"----- {album} -----"))
                            for song in db.interact(f'SELECT songid, title, createdby, filelocation, explicit FROM song NATURAL JOIN albumsongs WHERE playlistid = \'{aid}\''):
                                song = Song(*song)
                                artistSubmenu.append_item(cmi.FunctionItem(song.name, song.play))   
                        searchMenuTop.append_item(cmi.SubmenuItem(artist_display_name, artistSubmenu))
                    searchMenuTop.append_item(BlankItem(""))

                # Display all album results
                elif entry[0] == "album":
                    searchMenuTop.append_item(cmi.MenuItem("----- Albums -----"))
                    for aid, title, artist in entry[1]:
                        albumSubmenu = cm.ConsoleMenu(f"Album: {title}, Created by: {artist}")
                        for song in db.interact(f'SELECT songid, title, createdby, filelocation, explicit FROM song NATURAL JOIN albumsongs WHERE playlistid = \'{aid}\''):
                            song = Song(*song)
                            albumSubmenu.append_item(cmi.FunctionItem(song.name, song.play))   
                        searchMenuTop.append_item(cmi.SubmenuItem(title, albumSubmenu))
                    searchMenuTop.append_item(BlankItem(""))

                # Display all user playlist results
                elif entry[0] == "playlist":
                    searchMenuTop.append_item(cmi.MenuItem("----- User Playlists -----"))
                    for pid, title, creator in entry[1]:
                        playlistSubmenu = cm.ConsoleMenu(f"Playlist: {title}, Created by: {creator}")
                        for song in db.interact(f'SELECT songid, title, createdby, filelocation, explicit FROM song NATURAL JOIN userplaylistsongs WHERE playlistid = \'{pid}\''):
                            song = Song(*song)
                            playlistSubmenu.append_item(cmi.FunctionItem(song.name, song.play))   
                        searchMenuTop.append_item(cmi.SubmenuItem(title, playlistSubmenu))
                    searchMenuTop.append_item(BlankItem(""))

                # Display all user results
                elif entry[0] == "user":
                    searchMenuTop.append_item(cmi.MenuItem("----- Users -----"))
                    for username in [e.strip("'") for i in entry[1] for e in i]:
                        userSubmenu = cm.ConsoleMenu(username)
                        for pid, title in db.interact(f'SELECT playlistid, title from userplaylist JOIN users ON creator=username WHERE creator = \'{username}\''):
                            userSubmenu.append_item(cmi.MenuItem(f"----- {title} -----"))
                            for song in db.interact(f'SELECT songid, title, createdby, filelocation, explicit FROM song NATURAL JOIN userplaylistsongs WHERE playlistid = \'{aid}\''):
                                song = Song(*song)
                                userSubmenu.append_item(cmi.FunctionItem(song.name, song.play))   
                        searchMenuTop.append_item(cmi.SubmenuItem(username, userSubmenu))

                searchMenuTop.append_item(BlankItem(""))
            searchMenuTop.show()
    except:
        import traceback
        print(traceback.format_exc())
        input()
