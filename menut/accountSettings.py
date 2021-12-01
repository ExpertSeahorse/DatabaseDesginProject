import consolemenu as cm
import consolemenu.items as cmi
import db

from objects import User

def updateSetting(user, setting):
    if setting == 'name':
        print("This value cannot be changed.")
        input("Please press <Enter> to continue")
        return
    print(f"Enter a new value for your {setting}")
    newValue = input()
    setattr(user, setting, newValue)
    db.interact(f"UPDATE users SET {setting.lower()}={newValue} WHERE username={user.name}")
    buildAccountMenu(user)


def buildAccountMenu(user:User):
    accountMenuTop = cm.ConsoleMenu("Account Settings", "Choose an option to assign it a new value")
    accountMenuTop.append_item(cmi.FunctionItem(f"Username:       {user.name}", updateSetting, [user, "name"]))
    accountMenuTop.append_item(cmi.FunctionItem(f"First Name:     {user.firstName}", updateSetting, [user, "firstName"], should_exit=True))
    accountMenuTop.append_item(cmi.FunctionItem(f"Last Name:      {user.lastName}", updateSetting, [user, "lastName"], should_exit=True))
    accountMenuTop.append_item(cmi.FunctionItem(f"Date of Birth:  {user.dob}", updateSetting, [user, "dob"], should_exit=True))
    accountMenuTop.append_item(cmi.FunctionItem(f"Country:        {user.country}", updateSetting, [user, "country"], should_exit=True))

    if user.kind == 'g': kind = 'Guest'
    elif user.kind == 'p': kind = 'Premium'
    elif user.kind == 'a': kind = "Artist"
    else: kind = "NaN"
    accountMenuTop.append_item(cmi.FunctionItem(f"Subscription:   {kind}", updateSetting, [user, "kind"], should_exit=True))

    # Add followers/following to menu
    followers = cm.SelectionMenu(user.followers)
    following = cm.SelectionMenu(user.following)
    accountMenuTop.append_item(cmi.SubmenuItem("Followers", followers, accountMenuTop))
    accountMenuTop.append_item(cmi.SubmenuItem("Following", following, accountMenuTop))
    accountMenuTop.show()
