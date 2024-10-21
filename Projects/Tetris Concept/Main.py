def CreateBoard():
    Board = []
    Part = ' '
    for i in range(24):
        Row = []
        for j in range(10):
            Row.append(Part)
        Board.append(Row)
    return Board
