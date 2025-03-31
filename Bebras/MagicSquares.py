def CheckHorVer(Grid):
    for j in range(3):
        tot = 0
        tot2 = 0
        for i in range(3):
            tot += Grid[j][i]
            tot2 += Grid[i][j]
        if tot != 15:
            return False
        if tot2 != 15:
            return False
    return True

def CheckDiag(Grid):
    Total = 0
    for i in range(3):
        for j in range(3):
            if i == j:
                Total += Grid[i][j]
    if Total != 15:
        return False
    x = 0
    y = 2
    Total = 0
    for i in range(3):
        Total += Grid[y][x]
        y -= 1
        x += 1
    if Total != 15:
        return False
    return True

Grid = []
for i in range(3):
    Row = input()
    Grid.append(Row)
Real = []
for i in Grid:
    Correct = []
    j = i.split(' ')
    for k in j:
        Correct.append(int(k))
    Real.append(Correct)

HorVer = CheckHorVer(Real)
if not HorVer:
    print('muggle')
else:
    Diags = CheckDiag(Real)
    if Diags:
        print('magic')
    else:
        print('muggle')

        