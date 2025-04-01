Large = 0
Small = 0
Stock = int(input())
Done = False
while not Done:
    Full = False
    while not Full:
        if Stock - 24 > 0:
            Large += 1
            Stock -= 24
        else:
            Full = True
    if Stock <= 0:
        Done = True
    else:
        Stock -= 5
        Small += 1
print(Large, Small)