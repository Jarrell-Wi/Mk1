import random
def draw(hand):
    choice = input('Would you like to draw Y/N: ')
    if choice == 'Y':
        gain = random.randrange(1,10)
        hand.append(gain)
    return(hand)
def total(Check):
    sum = 0
    for i in range(len(Check)):
        sum = sum + (Check[i-1])
    return(sum)
Dealer = []
Player = []
for i in range(2):
    draw = random.randrange(1,11)
    Player.append(draw)
    draw = random.randrange(1,11)
    Dealer.append(draw)
print('Your total: ' + str(total(Player)))
print('Dealer shows (one card down): ' + str(Dealer[0]))