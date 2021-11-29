import consolemenu as cm
import consolemenu.items as cmi


from objects import User
from customMenuRows import BlankItem
from menut.playlists import buildPlaylistMenu
from menut.accountSettings import buildAccountMenu
from menut.search import buildSearch

# from temp_users import userGuest, userPrem, userArtist

print("Please log in")

# TODO: DB Login functionality
user = User("temp", "pass", "email", "dob", "country", "p", ["dave", "jeff", "kate"], ["Avicii", "Taylor Swift", "Jay Z"])
user.name = input()

# Build submenus
accountMenuTop = buildAccountMenu(user)
playlistMenuTop = buildPlaylistMenu(user)

# Create the menu
menu = cm.ConsoleMenu("Music Manager", f"Welcome {user.name}")
# menu.formatter = cm.MenuFormatBuilder(max_dimension=cm.menu_component.thin)

# Create submenus for each level of the tree
menu.append_item(cmi.SubmenuItem("Account Settings", accountMenuTop, menu))
menu.append_item(cmi.FunctionItem("Search", buildSearch, menu=menu))
if user.kind == "p":
    menu.append_item(cmi.SubmenuItem("Playlists", playlistMenuTop, menu))
elif user.kind == "a":
    menu.append_item(cmi.SubmenuItem("Albums", albumMenuTop, menu))

menu.append_item(BlankItem(""))

menu.show()