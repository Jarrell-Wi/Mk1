def Start():
    DisplayMenu()
    Choice = GetChoice()
    if Choice ==1:
        print('Starting Game')
    if Choice ==2:
        print('Open LeaderBoard Text File')
    if Choice ==3:
        print('Open Save File for player or create')
    if Choice ==4:
        print('WIP Function')
    if Choice ==9:


def DisplayMenu():
    print('Welcome to Tic Tac Toe :D')
    print()
    print('1 - Start New Game')
    print()
    print('2 - View LeaderBoard')
    print()
    print('3 - View Personal Game History')
    print()
    print('4 - WIP')
    print()
    print('9 - Quit')

def GetChoice():
    Chosen = True
    while Chosen:
        Choice = input('Enter Choice: ')
        try:
            Choice = int(Choice)
            if Choice >= 0 and Choice <= 4 or Choice == 9:
                Chosen = False
            else:
                print()
                print('Invalid Choice')
                print('Enter a Number Shown on Menu')
                print()
        except:
            print()
            print('Invalid Choice')
            print('Enter a Number Shown on Menu')
            print()
    return Choice


def PrintBoard(Board):
    for i in range(len(Board)):
        print(Board[i])

def CreateBoard():
    Board = []
    Rows = []
    for j in range(3):
        Rows.append('-')
        Board.append(Rows)
    return Board




Start()