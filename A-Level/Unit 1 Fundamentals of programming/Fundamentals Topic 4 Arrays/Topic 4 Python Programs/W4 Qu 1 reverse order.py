# Worksheet 4 Task 1 Qu 1
total = 0
#initialise array
numbers = [0,0,0,0,0,0]
for index in range (6):
    numbers[index] = input("Enter an integer number: ")
    n = int(numbers[index])
    total = total + n

for index in range (6):
    print(numbers[index],end = " ")
#now output the numbers in reverse order
print("\n\nHere are the numbers in reverse order\n")

for i in range(5,-1,-1):    
    print(numbers[i],end=" ")   # "end parameter prints  without moving to a new line 
print("")
print ("\nTotal = ",total)
average = round(total/6,2)
print("Average =",average)
    
input("\nPress Enter to end ")