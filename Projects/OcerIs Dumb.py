def start(user):
    checksave(user)

def checksave(user):
    try:
        file = open("./UserSaves/PlayerData - " + user, "r")
        print('Save Found')
    except:
        print('No Save')
        file = open("./UserSaves/PlayerData - " + user, "w+")
user = input('Enter Username: ')
start(user)
