def Start():
    DisplayMenu()
    Choice = GetChoice()
    if Choice ==1:
        print('|---------------------|')
        GameType, dif = GameModes()
        print('Gametype is', GameType, 'and Game Difficulty is', dif)
        print('Starting Game')
        if GameType == 'M':
            Multiplayer()
        else:
            Singleplayer(dif)

    if Choice ==2:
        print('Open LeaderBoard Text File')
    if Choice ==3:
        print('Open Save File for player or create')
    if Choice ==4:
        print('WIP Function')
    if Choice ==9:
        Quit()

def GameModes():
    Choices = 2
    print()
    print('1 - Single Player')
    print()
    print('2 - Multiplayer')
    print()
    Valid = False
    while not Valid:
        try:
            choice = int(input('Enter Choice: '))
            if choice < 1 or choice > Choices:
                print()
                print('Please Enter a Number Displayed Within the Options.')
            else: 
                Valid = True
        except:
            print()
            print('Please Enter a Number Displayed Within the Options.')
    if choice == 2:
        return('M', 'Player')
    else:
        Difficulty = False
        print()
        print('Select Computer Difficulty')
        print()
        print('1 - Easy')
        print()
        print('2 - Medium')
        print()
        print('3 - Hard')
        while not Difficulty:
            print()
            try:
                print()
                opponent = int(input('Enter Computer Difficulty: '))
                if opponent < 1 or opponent > 3:
                    print()
                    print('Enter a Difficulty Displayed on the Menu')
                else:
                    return('C', opponent)
            except:
                print()
                print('Enter Difficulty Displayed on the Menu')

def CheckWin(Board):
    choice = input('Win Y/N?')
    if choice == 'Y':
        print(Board)
        return True
    if choice == 'N':
        return False
        
def GetRowColumn(Board):
    Row = 10
    Column = 10
    while Row > 3 or Row < 1 or Column > 3 or Column < 1:
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

def PlayerMove(Board, Player):
    Valid = False
    while not Valid:
        Row, Column = GetRowColumn(Board)
        Valid = CheckValid(Board, Row, Column)
    print('Move Executed')
    Board[Row - 1][Column - 1] = Player
    return(Board)

def CheckValid(Board, Row, Column):
    if Board[Row - 1][Column - 1] != '-':
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
        print()
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
    print('The Board Looks Like this')
    print()
    for i in range(3):
        print(' | ' + Board[i][0] + ' | ' + Board[i][1]  + ' | ' + Board[i][2] + ' | ')

def CreateBoard():
    Board = []
    for i in range(3):
        Rows = []
        for j in range(3):
            Rows.append('-')
        Board.append(Rows)
    return Board

def Multiplayer():
    Board = CreateBoard()
    GameWon = False
    while not GameWon:
        Player = '0'
        Board = PlayerMove(Board, Player)
        if CheckWin(Board) == True:
            break
        Player = 'X'
        Board = PlayerMove(Board, Player)
        if CheckWin(Board) == True:
            break

def Singleplayer(Difficulty):
    return True
    
Start()