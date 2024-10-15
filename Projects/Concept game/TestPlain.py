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
        full = 'Hor' + str(i + 1) + ' prob' + str(prob)
        outcomes.append(full)
    return outcomes

def CheckVer(Board, Player):
    outcomes = []
    for i in range(3):
        prob = 0
        for j in range(3):
            if Board[j][i] == Player:
                prob += 1
        full = 'Ver' + str(i + 1) + ' prob' + str(prob)
        outcomes.append(full)
    return outcomes
        

Board = CreateBoard()
Player = 'X'
Board[0][0] = Player
Board[0][1] = Player
horizontals = CheckHor(Board, Player)
verticals = CheckVer(Board, Player)
print(horizontals)
print(verticals)