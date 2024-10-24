def FindBestProb(Set):
    Max = 0
    Best = []
    for i in range(len(Set)):
        if Max < Set[i]:
            Max = Set[i]
    Best.append(Max)
    for i in range(len(Set)):
        Small = []
        if Set[i] == Max:
            Best.append(i)
    return Best
Set = [2, 2, 1]
Highest = FindBestProb(Set)
print(Highest)