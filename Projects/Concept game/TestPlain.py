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
        order = []
        for j in range (3):
            if Board[i][j] == Player:
                order.append('1')
            else:
                order.append('0')
        full = 'H' + str(i + 1) + '-' + order[0] + order[1] + order[2]
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
        full = 'V' + str(i + 1) + '-' + order[0] + order[1] + order[2]
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
    full = 'DL' + '-' + order[0] + order[1] + order[2]
    outcomes.append(full)

    order = []
    for i in range(3):
        if Board[x][y] == Player:
            order.append('1')
        else:
            order.append('0')
        x -= 1
        y += 1
    full = 'DR' + '-' + order[0] + order[1] + order[2]
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
Board[2][0] = Player
Board[1][1] = Player
Board[1][2] = Player
PrintBoard(Board)
horizontals = CheckHor(Board, Player)
verticals = CheckVer(Board, Player)
Diags = CheckDiag(Board, Player)
print(horizontals)
print(verticals)
print(Diags)