def CollectNum(Num, pos):
    set = str(Num)
    while len(set) < pos:
        Num += 1
        set += str(Num)       
    print(set)
    print(set[pos - 1])
    return set
def GetNum(set):
    ctr = 0
    search = int(input('Enter Num to find: '))
    for i in range(len(set)):
        if set[i] == str(search):
            ctr += 1
    print(ctr)
Num = int(input('Enter Number: '))
Pos = int(input('Enter ith Position: '))
set = CollectNum(Num, Pos)
GetNum(set)

