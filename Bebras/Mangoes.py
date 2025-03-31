days = int(input())
old = 0
new = 0
ctr = 0
for i in range(days):
    BuySell = input()
    BuySell = BuySell.split(' ')
    new += int(BuySell[0])
    for i in range(int(BuySell[1])):
        if old - 1 < 0:
            new -= 1
            ctr += 1
        else:
            old -= 1
    old += new
    new = 0
print(ctr)   