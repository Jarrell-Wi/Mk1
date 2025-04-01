import random
Players = [[],[],[],[]]
Cards = input()
Deck = Cards.split(' ')
Set = []
for i in Deck:
    Set.append(i)
type = 0
for i in range(len(Set)):
    Card = random.randint(0, len(Set) - 1)
    Players[type].append(Set[Card])
    if type + 1 > 3:
        type = 0
    else:
        type += 1
    Set.remove(Set[Card])
string = ''
for i in Players[0]:
    string += i +' '

print(string[0:len(string) - 1])