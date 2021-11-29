import consolemenu as cm
import consolemenu.items as cmi

from customMenuRows import BlankItem

# TODO: edit user in db
def updateSetting(user, setting):
    print(f"Enter a new value for your {setting}")
    setattr(user, setting, input())

def buildAccountMenu(user):
    accountMenuTop = cm.ConsoleMenu("Account Settings", "Choose an option to edit it")
    accountMenuTop.append_item(cmi.FunctionItem(f"Name:           {user.name}", updateSetting, [user, "name"], None, accountMenuTop))
    accountMenuTop.append_item(cmi.FunctionItem(f"Password:       {user.passw}", updateSetting, [user, "passw"]))
    accountMenuTop.append_item(cmi.FunctionItem(f"Email:          {user.email}", updateSetting, [user, "email"]))
    accountMenuTop.append_item(cmi.FunctionItem(f"Date of Birth:  {user.dob}", updateSetting, [user, "dob"]))
    accountMenuTop.append_item(cmi.FunctionItem(f"Country:        {user.country}", updateSetting, [user, "country"]))
    accountMenuTop.append_item(BlankItem(""))

    followers = cm.SelectionMenu(user.followers)
    following = cm.SelectionMenu(user.following)
    accountMenuTop.append_item(cmi.SubmenuItem("Followers", followers, accountMenuTop))
    accountMenuTop.append_item(cmi.SubmenuItem("Following", following, accountMenuTop))
    return accountMenuTop
# accountMenuTop.append_item(cmi.FunctionItem(f"", updateSetting, [user, ""]))