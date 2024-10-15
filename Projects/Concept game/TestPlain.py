def CreateBoard():
    Board = []
    for i in range(3):
        Rows = []
        for j in range(3):
            Rows.append('-')
        Board.append(Rows)
    return Board

def CheckHor(Board, Player):
    outcomes = []
    for i in range(3):
        prob = 0
        for j in range (3):
            if Board[i][j] == Player:
                prob +=1
        full = 'H' + str(i + 1) + '' + str(prob)
        outcomes.append(full)
    return outcomes

def CheckVer(Board, Player):
    outcomes = []
    for i in range(3):
        prob = 0
        for j in range(3):
            if Board[j][i] == Player:
                prob += 1
        full = 'V' + str(i + 1) + 'prob' + str(prob)
        outcomes.append(full)
    return outcomes


def CheckDiag(Board, Player):
    outcomes = []
    prob = 0
    x = 2
    y = 0
    for i in range(3):
        if Board[i][i * (-1)] == Player:
            prob += 1
    full = 'DL prob' + str(prob)
    outcomes.append(full)

    prob = 0
    for i in range(3):
        if Board[x][y] == Player:
            prob += 1
        x -= 1
        y += 1
    full = 'DR prob' + str(prob)
    outcomes.append(full)
    return outcomes



def PrintBoard(Board):
    print()
    print('The Board Looks Like this')
    print()
    for i in range(3):
        print(' | ' + Board[i][0] + ' | ' + Board[i][1]  + ' | ' + Board[i][2] + ' | ')

Board = CreateBoard()
Player = 'X'
Board[0][0] = Player
Board[0][1] = Player
Board[0][2] = Player
PrintBoard(Board)
horizontals = CheckHor(Board, Player)
verticals = CheckVer(Board, Player)
Diags = CheckDiag(Board, Player)
print(horizontals)
print(verticals)
print(Diags)