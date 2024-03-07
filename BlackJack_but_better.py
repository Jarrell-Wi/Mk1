import random
Exit = False
class cards:
    def __init__(Place):
        Place.Hasace = 0
        card1 = random.randrange(1,10)
        card2 = random.randrange(1,10)
        Place.hand = card1, card2
        for i in range(len(Place.hand)):
            if Place.hand[i] == 1:
                print(Place.hand[i])
                Place.Hasace += 1

    def CheckHand (Place):
            for i in range (len(Place.hand)):
                tot = tot + place.hand[i]
            if tot + 10 > 21:
                return False
            if tot + 10 <= 21:
                return True

    def draw (Place):
        card = random.randrange(1,10)
        print(len(Place.hand))
        if card == 1:
            if Place.CheckHand():
                card = card + 10
                Place.Hasace +=1
            else:
                Place.Hasace +=1
        Place.hand.append(card)
    def PrintHand(Place):
        for each in Place.hand:
            if each == 11:
                print(each, " - Ace")


if __name__ == "__main__":
    while not Exit:
        Start = input('Play blackjack? Y/N ').upper()
        if Start == 'Y':
            player = cards()
            dealer = cards()
            print(player.PrintHand())
            print(dealer.PrintHand())
            print(player.hand,player.Hasace)
            print(dealer.hand,dealer.Hasace)
        else:
            Exit = True
print('Game ended.')