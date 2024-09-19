def read(name):
    file = open(f'{name}.txt', 'w+')
    data = file.read()
    print(data)
    file.close()
    print()
    start(name)
    
def add(name):
    file = open(f'{name}.txt', 'a')
    data = input('Enter Score: ')
    file.write(data + '\n')
    file.close()
    print()
    start(name)
    
def clear(name):
    file = open(f'{name}.txt', 'w')
    file.write('')
    file.close()
    print()
    start(name)

def highscore(name):
    scores = []
    file = open(f'{name}.txt', 'r')
    for i in file:
        a = int(i)
        scores.append(a)
    highest = 0
    for i in range(len(scores)):
        if scores[i] >= highest:
            highest = scores[i]
    print(f'Highest Score is {highest}')
    start(name)
    
def quit():
    return('Application Closed.')



def start(name):
    print('1 - Read Scores')
    print('2 - Add Scores')
    print('3 - Clear Data')
    print('4 - Highscore')
    print('5 - Quit')
    choice = input('What do you want to do? ')
    print()
    
    if choice == '1':
        read(name)
    if choice == '2':
        add(name)
    if choice == '3':
        clear(name)
    if choice == '4':
        highscore(name)
    if choice == '5':
        print(quit)

        
print('Welcome to Score thingy :D')
name = input('Enter name: ')

start(name)


