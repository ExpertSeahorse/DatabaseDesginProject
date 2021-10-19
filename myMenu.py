import consolemenu as cm

from temp_users import userGuest, userPrem, userArtist

invalidUser = True
while invalidUser:
    invalidUser = False
    usern = input("Username: ")
    passw = input("Password: ")

    # Build SQL User signin script
    # user = signIn(usern, passw)

    # Temp "signin"
    if usern.lower()[0] == "g":
        user = userGuest
    elif usern.lower()[0] == "p":
        user = userPrem
    elif usern.lower()[0] == "a":
        user = userArtist
    else:
        print("Invalid username or password.")
        invalidUser = True



# Create the menu
menu = cm.ConsoleMenu("DBDesign Project", "Music Manager")

# Create submenus for each of the different functions
topMenu=["Profile", "Search", "Create Playlist"]

for entry in topMenu:
    menu.append_item(cm.items.MenuItem(entry))

menu.show()