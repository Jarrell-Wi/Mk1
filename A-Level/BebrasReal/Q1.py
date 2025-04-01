Rice = int(input())
Amount = 1
ctr = 0
while Rice > Amount:
    Rice -= Amount
    Amount += Amount
    ctr += 1
print(ctr)1