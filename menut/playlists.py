import json
import consolemenu as cm
import consolemenu.items as cmi

from customMenuRows import BlankItem

def playPlaylist(playlist, song):
    try:
        i = playlist.songs.index(song)
        songs = [ {'name': song.name, 'artist': song.artist, 'path': song.path} for song in playlist.songs[i:] ]
        with open("playlist", 'w') as fout:
            json.dump(songs, fout)
        playlist.songs[i].play()
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        input()



def buildPlaylistMenu(user):
    playlistMenuTop = cm.ConsoleMenu("Playlists", "How to interact")

    # TODO: Get playlist list from db
    for playlist in user.playlists:
        playlistItem = cm.ConsoleMenu(playlist.name)
        for song in playlist.songs:
            playlistItem.append_item(cmi.FunctionItem(song.name, playPlaylist, [playlist, song], menu=playlistItem))

        playlistMenuTop.append_item(cmi.SubmenuItem(playlist.name, playlistItem, playlistMenuTop))
    return playlistMenuTop
