#AS AQA unit 1 W4 Q5 grid
#initialise grid
grid = []
for row in range(0,6):
    grid.append([])
    for column in range(0,4):
        grid[row].append("x")
        
# set character position top left and print grid
grid[0][0]="O"
for row in range(0,6):
    
    for column in range(0,4):
        print (grid[row][column],end ="  ")
    print()
#clear the grid
grid[0][0] = "x"

#now specify a position to move character to
row = int(input("\nEnter row to move to (1-6): "))-1
column = int(input ("Enter column to move to (1-4): "))-1
print()
grid[row][column] = "O"


for row in range(0,6):
    for column in range(0,4):
        symbol = grid[row][column]
        print (symbol,' ', end='')
    print()
#end='' stops Python  from moving to a new line after printing

input("\nPress Enter to end ")