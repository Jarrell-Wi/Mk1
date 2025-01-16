placeholder = " "
def find(board,choice):
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if choice == board[i][j]:
                return i, j
fill = ['a', ' ', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' ]
grid = []

def CreateGrid():
    print('Max size 6 x 4')
    columns = int(input('Enter Columns: '))
    rows = int(input('Enter Rows: '))
      

    return()

def SaveData():
    with open('Board.txt', 'w') as GameSave:
        GameSave.write(str(grid))

def LoadData():
    with open('Board.txt', ' r') as GameSave:
        grid = GameSave.readline()




def show(board):
    for i in range(len(board)):
        print(grid[i])

while True:
    Columns = int(input('How many columns: '))
    rows = int(input('How many rows: '))
    CreateGrid()
    show(grid)
    choice = input("Enter a letter: ").lower()
    if choice == 'save':
        SaveData()
    elif choice == 'load':
        LoadData()
    direction = input("Enter a direction (u,d,l,r): ")

    row, column = find(grid, choice)

    if direction == "r":
        if column + 2 < len(grid[0]):
            if grid[row][column + 2] == placeholder:
                grid[row][column] = placeholder
                grid[row][column + 1] = placeholder
                grid[row][column + 2] = choice

    elif direction == "l":
        if column - 2 >= 0:
            if grid[row][column - 2] == placeholder:
                grid[row][column] = placeholder
                grid[row][column - 1] = placeholder
                grid[row][column - 2] = choice

    elif direction == "u":
        if row - 2 >= 0:
            if grid[row - 2][column] == placeholder:
                grid[row][column] = placeholder
                grid[row - 1][column] = placeholder
                grid[row - 2][column] = choice

    elif direction == "d":
        if row + 2 < len(grid):
            if grid[row + 2][column] == placeholder:
                grid[row][column] = placeholder
                grid[row + 1][column] = placeholder
                grid[row + 2][column] = choice         
