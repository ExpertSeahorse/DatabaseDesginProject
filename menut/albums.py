import os
import consolemenu as cm
import consolemenu.items as cmi

import db
from objects import User


def createAlbum(user: User):
    try:
        # Create Album
        album_id = db.interact('SELECT COUNT(*) FROM album;')[0][0] + 101
        title = input('Album Title: ')
        record_label = input('Record label: ')
        db.interact(f'INSERT INTO album VALUES ({album_id}, \'{title}\', 0, 0, \'{record_label}\', 0, \'{user.name}\');')
        print(f"Album: {title} has been created successfully")
        while True:
            print()
            # Create song
            song_id = db.interact('SELECT COUNT(*) from song;')[0][0] + 1
            while True:
                song_title = input("Song title (or 'done' to quit): ")
                if len(song_title) < 30:
                    break
                print("Title too long")

            if song_title.lower() == 'done':
                break

            while True:
                length = input('Length: ')
                try:
                    int(length)
                    break
                except ValueError:
                    print("Please enter the number of seconds of the song")
            
            while True:
                explicit = input('Explicit (1 for True/0 for False): ')
                try:
                    explicit = bool(explicit)
                    break
                except ValueError:
                    print("Please enter a 0 or 1")

            file_location = input('File location: ')
            db.interact(f'INSERT INTO song VALUES ({song_id}, \'{song_title}\', {length}, {explicit}, \'{file_location}\', \'{user.name}\');')

            # Add to album
            db.interact(f'INSERT INTO albumsongs VALUES ({album_id}, {song_id});')
            # Update playlist values (length, numsongs)
            playlist_length = int(db.interact(f'SELECT length FROM album WHERE playlistid = {album_id};')[0][0])
            # print(playlist_length)
            db.interact(f'UPDATE album SET length = {int(length) + playlist_length} WHERE playlistid = {album_id};')
            db.interact(f'UPDATE album SET numsongs = numsongs + 1 WHERE playlistid = {album_id};')
            print(f"Created song: {song_title}")
    except Exception:
        import traceback
        print(traceback.format_exc())
        input()


def _playlistAddSongs(playlist_id):
    try:
        while True:
            # Search for a song
            search = input("Enter the name of a song to add (or 'done' to quit): ")
            if search.lower() == 'done':
                break
            matches = db.interact(f'SELECT songid, title, createdby FROM song WHERE title LIKE \'%{search}%\';')
            if len(matches) == 0:
                print("No matches found, please try again.")
                continue

            print("\n\nEnter the id of the song you want to add: ")
            for songid, title, artist in matches:
                print(f"{songid}- {title}, by: {artist}")
            insert_id = input()

            # Add that song to the playlist
            db.interact(f'INSERT INTO userplaylistsongs VALUES ({playlist_id}, {insert_id});')
            song_length = int(db.interact(f'SELECT length FROM song WHERE songid = {insert_id};')[0][0])
            playlist_length = int(db.interact(f'SELECT length FROM userplaylist WHERE playlistid = {playlist_id};')[0][0])
            # Update playlist values (length, numsongs)
            db.interact(f'UPDATE userplaylist SET length = {song_length + playlist_length} WHERE playlistid = {playlist_id};')
            db.interact(f'UPDATE userplaylist SET numsongs = numsongs + 1 WHERE playlistid = {playlist_id};')
            os.system('cls' if os.name == 'nt' else 'clear')
    except Exception:
        import traceback
        print(traceback.format_exc())
        input()


def _playlistDelSongs(playlist_id, songid):
    db.interact(f"DELETE FROM userplaylistsongs WHERE playlistid = \'{playlist_id}\' AND songid = \'{songid}\'")

def createPlaylist(user: User):
    # Create a Playlist
    playlist_id = db.interact('SELECT COUNT(*) FROM userplaylist;')[0][0] + 1
    title = input('Playlist Title: ')
    db.interact(f'INSERT INTO userplaylist VALUES ({playlist_id}, \'{title}\', 0, 0, \'{user.name}\');')
    print(f"Playlist: \"{title}\" created successfully")

    _playlistAddSongs(playlist_id)
    

def editPlaylist(user: User):
    editPlaylistMenu = cm.ConsoleMenu("Edit playlists", "Select which playlist to edit")
    for pid, title in db.interact(f'SELECT playlistid, title FROM userplaylist WHERE creator = \'{user.name}\';'):
        playlistItem = cm.ConsoleMenu(title)
        playlistItem.append_item(cmi.FunctionItem("Add songs", _playlistAddSongs, [pid], should_exit=True))
        
        deleteItem = cm.ConsoleMenu(title, "Select a song to remove it from the playlist")
        for songid, stitle in db.interact(f'SELECT songid, title FROM song NATURAL JOIN userplaylistsongs WHERE playlistid = \'{pid}\''):
            deleteItem.append_item(cmi.FunctionItem(stitle, _playlistDelSongs, [pid, songid], should_exit=True))
        playlistItem.append_item(cmi.SubmenuItem("Delete Songs", deleteItem, playlistItem))
        editPlaylistMenu.append_item(cmi.SubmenuItem(title, playlistItem, editPlaylistMenu))
    editPlaylistMenu.show()
