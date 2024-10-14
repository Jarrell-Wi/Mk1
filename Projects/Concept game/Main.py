def Start():
    DisplayMenu()
    Choice = GetChoice()
    if Choice ==1:
        print()
        print('Starting Game')
        print()
        CreateMatch()
    if Choice ==2:
        print('Open LeaderBoard Text File')
    if Choice ==3:
        print('Open Save File for player or create')
    if Choice ==4:
        print('WIP Function')
    if Choice ==9:
        Quit()

def CreateMatch():
    GameWon = False
    Board = CreateBoard()
    while not GameWon:
        PlayerMove(Board)
        PlayerMove(Board)
        GameWon = CheckWin(Board)

def CheckWin(Board):
    return True
        

def GetRowColumn(Board):
    Row = 10
    Column = 10
    while Row > 3 or Row < 1 or Column > 3 or Column < 1:
        print('The Board Looks Like This.')
        PrintBoard(Board)
        try:
            print()
            Row = int(input('Enter Row of Choice: '))
            print()
            Column = int(input('Enter Column of Choice: '))
            if Row > 3 or Row < 1 or Column > 3 or Column < 1:
                print()
                print('Invalid Input')
                print('Please Enter a Position Within the Board')
        except:
            print()
            print('Invalid Input')
            print('Please Enter a Position Within the Board')
    return Row, Column


def PlayerMove(Board):
    Valid = False
    while not Valid:
        Row, Column = GetRowColumn(Board)
        Valid = CheckValid(Board, Row, Column)
    print('Move Executed')
    Board[Row - 1][Column - 1] = 'X'
    PrintBoard(Board)

def CheckValid(Board, Row, Column):
    if Board[Row][Column] != '-':
        return False
    else:
        return True

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

def Quit():
    print('Exiting Program...')

def PrintBoard(Board):
    print()
    j = 0
    for i in range(3):
        print(' | ' + Board[i][j] +' | ' + ' | ' + Board[i][j + 1] +' | ' + Board[i][j + 2] + ' | ')

def CreateBoard():
    Board = []
    for i in range(3):
        Rows = []
        for j in range(3):
            Rows.append('-')
        Board.append(Rows)
    return Board




Start()