#AS AQA unit 1 W4 Q6 car park
carPark = []
for row in range(0,10):
    carPark.append([])
    for column in range(0,6):
        carPark[row].append("empty    ")
#next statement is for test purposes
carPark[0][0] = "TAKEN    "
        
for row in range(0,10):
    for column in range(0,6):
        symbol = carPark[row][column]
        print (symbol,' ', end='')
    print()


print("Enter the car registration: ")
regNo = input()
#now specify a position where car is parked
row = int(input("Enter row where car is parked (1-10): "))
column = int(input ("Enter column where car is parked (1-6): "))
emptySpace = False

while emptySpace == False:

    while row < 1 or row > 10:
        row = int(input("Row must be between 1 and 10 - please re-enter: ")) 
    row = row - 1
    rowValid = True
    
    while column < 1 or column > 6:
        column = int(input("Column must be between 1 and 6 - please re-enter: "))
    column = column - 1
    columnValid = True
    if rowValid and columnValid and carPark[row][column]== "empty    ":
        emptySpace = True
    else:
        rowValid = False
        columnValid = False
        print ("\nThat space is taken\n")  #\n goes to next line
carPark[row][column] = regNo

for row in range(0,10):
    for column in range(0,6):
        symbol = carPark[row][column]
        print (symbol,' ', end = '')       #end ='' stays on same line
    print()

input("\nPress Enter to end ")