def GeneratePalins(num):
    set = []
    for i in range(1, num):
        potent = str(i)
        if potent == potent[::-1]:
            set.append(int(potent))
    return set

def CheckPalin(num):
    num = str(num)
    if num [::-1] == num:
        return True
    return False

def FindPalin(num):
    solutions = []
    goal = num
    PalinsSet = GeneratePalins(num)
    
    if CheckPalin(num):
        return[num]
    found = {}
    for i, number in enumerate(PalinsSet):
        secnum = num - PalinsSet[i]
        if secnum in found:
            print(secnum, PalinsSet[i])
        else:
            found[number] = i
    Nums = []
    for i in found.keys():
        Nums.append(i)
    print(Nums)
    possible = []

    found = {}
    for i, number in enumerate(PalinsSet):
        for j, number in enumerate(PalinsSet):
            second = num - (PalinsSet[i] + PalinsSet[j])
            if second in found:
                possible.append((PalinsSet[i], PalinsSet[j], second))
            else:
                found[number] = i
    return possible

        



Fair = False
while not Fair:
    Number = int(input('Enter number to find palindrom equation: '))
    if Number > 0 and Number <= 1000000:
        Fair = True
Options = FindPalin(Number)
print(Options)