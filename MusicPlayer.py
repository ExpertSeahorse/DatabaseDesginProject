import sys
import vlc
import json
import os
import consolemenu as cm
import consolemenu.items as cmi

def volume(dir, mp):
    if dir:
        mp.audio_set_volume(mp.audio_get_volume()+10)
    else:
        mp.audio_set_volume(mp.audio_get_volume()-10)


try:
    songs = []
    try:
        with open("playlist", 'r') as fin:
            songs = json.load(fin)
        os.remove('playlist')
    except FileNotFoundError:
        songs.append({'name': sys.argv[1], 'path': sys.argv[2]})

    firstSong = True
    for i in range(len(songs)):
        song = songs[i]
        # TODO: Remove this and rely of song's own path
        song['path'] = "C:\\Users\\dtfel\\Downloads\\Girl_Talk_-_All_Day_(IA123)_mp3s\\Girl Talk - All Day (IA123)\\01 - Girl Talk - Oh No.mp3"
        mp = vlc.MediaPlayer(song['path'])
        if firstSong:
            mp.audio_set_volume(50)
            firstSong = False
        mp.play()

        prog = None
        if i < len(songs)-1:
            prog = f"Next Song: {songs[i+1]['name']}"    
        
        menu = cm.ConsoleMenu("Now Playing", song['name'], prologue_text=prog)
        menu.append_item(cmi.FunctionItem(f"Play", mp.play, menu=menu))
        menu.append_item(cmi.FunctionItem(f"Pause", mp.pause, menu=menu))
        menu.append_item(cmi.FunctionItem(f"Volume Down", volume, [False, mp],  menu=menu))
        menu.append_item(cmi.FunctionItem(f"Volume Up", volume, [True, mp], menu=menu))
        menu.exit_item = cmi.ExitItem("Skip")
        menu.show()

        mp.stop()
except Exception as e:
    import traceback
    print(traceback.format_exc())
    input()
