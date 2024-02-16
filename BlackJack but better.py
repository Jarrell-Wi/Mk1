import random
class cards:
    def __init__(Place):
        Place.Hasace = 0
        card1 = random.randrange(1,10)
        card2 = random.randrange(1,10)
        Place.hand = card1, card2
        for i in range(len(Place.hand)):
            if Place.hand[i] == 1:
                Place.Hasace += 1
    def draw (Place):
        card = random.randrange(1,10)
        Place.hand.append(card)
        print(len(Place.hand))
        if card == 1:
            Place.Hasace +=1

player = cards()
dealer = cards()
print(player.hand,player.Hasace)
print(dealer.hand,dealer.Hasace)