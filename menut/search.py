import consolemenu as cm
import consolemenu.items as cmi

from objects import Song, songs

def buildSearch():
    try:
        search = input("Search> ").lower()
        found = []
        for song in songs:
            if song.match(search):
                entry = []
                entry.append(song)            
                if search in song.name.lower():
                    entry.append("song")
                elif search in song.artist.lower():
                    entry.append("artist")
                found.append(entry)
        if len(found) == 0:
            found.append([Song("Not Found", "", None), ""])
            
        if found[0][0].name == "Not Found":
            searchMenuTop = cm.ConsoleMenu("Search", f"{search}", prologue_text=f"{search} does not match any song or artist names")
            searchMenuTop.append_item(cmi.FunctionItem("Search Again", buildSearch, menu=searchMenuTop, should_exit=True))
            searchMenuTop.show()
        else:
            searchMenuTop = cm.ConsoleMenu("Search", f"{search}")
            for entry in found:
                if entry[1] == "song":
                    searchMenuTop.append_item(cmi.FunctionItem(entry[0].name, entry[0].play))   
                elif entry[1] == "artist":
                    artistSubmenu = cm.ConsoleMenu(entry[0].artist)
                    for song in songs:
                        if song.artist == entry[0].artist:
                            artistSubmenu.append_item(cmi.FunctionItem(song.name, song.play))   
                    searchMenuTop.append_item(cmi.SubmenuItem(entry[0].artist, artistSubmenu))
            searchMenuTop.show()
    except:
        import traceback
        print(traceback.format_exc())
        input()
