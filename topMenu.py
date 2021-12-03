import consolemenu as cm
import consolemenu.items as cmi
import db
import sys

from objects import User
from customMenuRows import BlankItem
from menut.playlists import buildPlaylistMenu
from menut.accountSettings import buildAccountMenu
from menut.search import buildSearch

# from temp_users import userGuest, userPrem, userArtist

# Get username
while True:
    if len(sys.argv) > 1 and sys.argv[1] == 'd':
        uname = "HaroldMusic"
    else:
        uname = input("Username: ") 
    resp = db.interact(f"SELECT * FROM users WHERE username='{uname}'")
    if resp != []:
        resp = resp[0]
        break
    print("That username not found, please try again")

# Get rank
curr_user = resp[0]
if db.interact(f"SELECT * FROM guest WHERE username='{curr_user}'") != []:
    kind = 'g'
elif db.interact(f"SELECT * FROM premium WHERE username='{curr_user}'") != []:
    kind = 'p'
elif db.interact(f"SELECT * FROM artist WHERE username='{curr_user}'") != []:
    kind = 'a'
else:
    print("Rank not found?")

# Get followers/following
following = db.interact(f'SELECT following FROM follows WHERE follower = \'{curr_user}\';')
follower = db.interact(f'SELECT follower FROM follows WHERE following = \'{curr_user}\';')

# Get playlists
playlists = db.interact(f'SELECT playlistid, title FROM userplaylist WHERE creator = \'{curr_user}\';')

# Build User for program to use
user = User(*resp, kind, follower, following, playlists)

# Create the menu
menu = cm.ConsoleMenu("Music Manager", "Welcome")

# Create submenus for each level of the tree
menu.append_item(cmi.FunctionItem("Account Settings", buildAccountMenu, [user], menu=menu))
menu.append_item(cmi.FunctionItem("Search", buildSearch, menu=menu))
if user.kind == "p":
    menu.append_item(cmi.FunctionItem("Playlists", buildPlaylistMenu, [user, 'p'], menu=menu))
elif user.kind == "a":
    menu.append_item(cmi.FunctionItem("Albums", buildPlaylistMenu, [user, 'a'], menu=menu))

menu.append_item(BlankItem(""))

menu.show()
