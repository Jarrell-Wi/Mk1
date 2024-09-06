import random
def stockchange(stockrate):
    stockpercent = random.randint(1,10)/100
    stocknew = stockrate * (stockpercent + 1)
    return(stocknew, stockpercent * 100)

def stockinvest(money, amount):
    print('1 - Mcdonalds')
    print('2 - Burger King')
    print('3 - Wigget Group')
    investment = int(input('where do you want to invest:'))
    print('Balance -', money)
    amount = int(input('How much: '))
    money -= amount
    return(investment, money, amount)

def startday(day, money):
    day+= 1
    messages = [f'It\'s day {day} lets get started.', f'Rise and shine it\'s day {day} time to start investing.', f'Gooday it\'s day {day}. Get the flippity dippity flop up and start investing YOU LAZY BASTARD!', 'Good morning sunshine, invest don\'t rest and get to it', f'Day {day} wow look how far we\'ve come, tired of investing yet? I DONT CARE DO YOU WANT YOUR LAPTOP FIXED OR NOT!','Get up! Your snooze button isn\'t going to press itself.',f'WAKE UP! Its day {day}, your pillow is begging for a break seriously.', f'Morning, it\'s day {day}! Your bed might miss you but the world won\'t. I promise.']
    choice = random.randint(0, len(messages) - 1)
    print(messages[choice])

    

def startgame():
    day = 0
    money = 1000
    print('Welcome to Bralfie Brant Simulator the hit investment game!')
    print('your goal is to make as much money as possible from your savings')
    print('so you can afford to pay to fix your super sick RGB gaming laptop')
    print('after it broke T-T. Good luck :D')
    startday(day, money)

startgame()


