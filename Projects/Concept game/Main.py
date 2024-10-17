import random
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

def CheckDraw(Board):
    filled = 0
    for i in range(3):
        for j in range(3):
            if Board[i][j] != '-':
                filled += 1
    if filled == 9:
        return True
    else:
        return False

def CheckWin(Board, Player):
    Horizontal = CheckHor(Board, Player)
    Vertical = CheckVer(Board, Player)
    Diagonal = CheckDiag(Board, Player)
    for i in range(3):
        if Horizontal[i] == '111':
            return True
        if Vertical[i] == '111':
            return True
    if Diagonal[0] == '111' or Diagonal[1] == '111':
        return True

def CheckHor(Board, Player):
    outcomes = []
    for i in range(3):
        order = []
        for j in range (3):
            if Board[i][j] == Player:
                order.append('1')
            else:
                order.append('0')
        full = order[0] + order[1] + order[2]
        outcomes.append(full)
    return outcomes

def CheckVer(Board, Player):
    outcomes = []
    for i in range(3):
        order = []
        for j in range(3):
            if Board[j][i] == Player:
                order.append('1')
            else:
                order.append('0')
        full = order[0] + order[1] + order[2]
        outcomes.append(full)
    return outcomes

def CheckDiag(Board, Player):
    outcomes = []
    order = []
    x = 2
    y = 0
    for i in range(3):
        if Board[i][i] == Player:
            order.append('1')
        else:
            order.append('0')
    full = order[0] + order[1] + order[2]
    outcomes.append(full)

    order = []
    for i in range(3):
        if Board[x][y] == Player:
            order.append('1')
        else:
            order.append('0')
        x -= 1
        y += 1
    full = order[0] + order[1] + order[2]
    outcomes.append(full)
    return outcomes

def GetRowColumn(Board):
    Row = 10
    Column = 10
    while Row > 3 or Row < 1 or Column > 3 or Column < 1:
        PrintBoard(Board)
        try:
            print()
            Column = int(input('Enter Column of Choice: '))
            print()
            Row = int(input('Enter Row of Choice: '))
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
    print()
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

def TestBoard():
    Board = CreateBoard()
    Board[1][1] = 'X'
    Board[0][1] = '0'
    Board[2][2] = '0'
    Board[1][2] = 'X' 
    PrintBoard(Board)

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

def GetType():
    Valid = False
    while not Valid:
        print('1 - Play as 0s')
        print()
        print('2 - Play as Xs')
        try:
            PlayerType = int(input('Choose Your Play Piece: '))
            if PlayerType == 1 or PlayerType == 2:
                Valid = True
            else:
                print()
                print('Enter a Number Shown Within the Displayed Options.')
                print()
        except:
            print()
            print('Enter a Number Shown Within the Displayed Options.')
            print()
    if PlayerType == 1:
        return('0', 'X')
    else:
        return('X', '0')

def EasyMove(Board, Computer):
    Valid = False
    while not Valid:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if CheckValid(Board, x, y) == True:
            Board[x - 1][y - 1] = Computer
            Valid = True
    return Board

def ComputerEasy():
    Board = CreateBoard()
    Player, Computer = GetType()
    Done = False
    while not Done:
        Board = PlayerMove(Board, Player)
        if CheckWin(Board, Player) == True:
            print()
            print('Congratulations Player.')
            PrintBoard(Board)
            print('You have Won!!!')
            break
        if CheckDraw(Board) == True:
            print()
            print('The Game is Over')
            PrintBoard(Board)
            print()
            print('You have Drawn')
            break
        Board = EasyMove(Board, Computer)
        print('Computer Places')
        if CheckWin(Board, Computer) == True:
            print()
            print('Game is Over.')
            PrintBoard(Board)
            print('The Computer has Won.')
            break
        if CheckDraw(Board) == True:
            print()
            print('The Game is Over')
            PrintBoard(Board)
            print()
            print('You have Drawn.')
            break
    Start()

def ComputerMedium():
    return True

def ComputerHard():
    return True
    
def Singleplayer(Difficulty):
    if Difficulty == 1:
        ComputerEasy()
    elif Difficulty == 2:
        ComputerMedium()
    else:
        ComputerHard()
    
def Multiplayer():
    Board = CreateBoard()
    GameWon = False
    while not GameWon:
        Player = 'X'
        Board = PlayerMove(Board, Player)
        if CheckWin(Board, Player) == True:
            print()
            print('Congratulations Player 1.')
            PrintBoard(Board)
            print('You have Won!!!')
            break
        if CheckDraw(Board) == True:
            print()
            print('The Game is Over')
            PrintBoard(Board)
            print()
            print('You have Drawn')
            break
        Player = '0'
        Board = PlayerMove(Board, Player)
        if CheckWin(Board, Player) == True:
            print()
            print('Congratulations Player 2.')
            PrintBoard(Board)
            print('You have Won!!!')
            break
        if CheckDraw(Board) == True:
            print()
            print('The Game is Over')
            PrintBoard(Board)
            print()
            print('You have Drawn')
            break
    Start()

TestBoard() 
Start()