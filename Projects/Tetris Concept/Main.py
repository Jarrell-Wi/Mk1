def CreateBoard():
    Board = []
    Part = '   '
    for i in range(24):
        Row = []
        for j in range(10):
            Row.append(Part)
        Board.append(Row)
    return Board

def PrintBoard(Board):
    for i in range(24):
        print(' |' + Board[i][0] + '|' + Board[i][1]  + '|' + Board[i][2] + '|' + Board[i][3] + '|' + Board[i][4] + '|' + Board[i][5] + '|' + Board[i][6] + '|' + Board[i][7] + '|'+ Board[i][8] + '|' + Board[i][9] + '|')
    return
def Start():
    Board = CreateBoard()
    PrintBoard(Board)

Start()