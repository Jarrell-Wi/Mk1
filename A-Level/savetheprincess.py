from random import randint
import random

size=2
while size%2==0:
    size=int(input("enter the grid size - must be an odd number: "))

board=[["-" for x in range(size)] for y in range(size)]
mid=(size//2)
board[mid][mid]="m"
princessx = random.randint(0,size)
princessy = random.randint(0,size)
board [princessx][princessy] = 'p'






for row in board:
    for e in row:
        print (e, end='')
    print()

print("Maurizio needs to rescue the Princess")

mariopos = mid
for i in range(len(board)):
    for j in range(len(row)):



#you need to write the code to solve the puzzle
# It should output the directions Maurizio needs to take to get to Princess Pineapple
# Directions should be output in the form "UP" "DOWN" "LEFT" "RIGHT"
# e.g. "UP" "UP" "LEFT" "LEFT" "LEFT"


#hints

# use nested for loops to find the princesses row and column
# calculate the difference between that co-ordinate and Maurizio
# output the correct command set