def start(user):
    checksave(user)

def checksave(user):
    try:
        file = open(f'{user}save', 'r')
        print('Save Found')
    except:
        print('No Save')


user = input('Enter Username: ')
start(user)
