#OCR unit 11 H4 Q3 name array

def displayMenu():
    #display menu of options
    print("\n1. Add name")
    print("2. Display list")
    print("3. Quit")
    
    option = int(input("\nEnter your choice: "))
    while option not in range(1,4):
        option = int(input ("Invalid choice - please re-enter: "))
    return option
#ENDSUB

def addName(names):
    print("Enter the name to be added to the list")
    newName = input()
    index = 11
    while not index in range(10):
        print("Enter the position in the list to insert the name (1-10): ")
        index = int(input())-1
        if index in range(10):
            names[index] = newName
        else:
            print("invalid entry - must be between 1 and 10")
#ENDSUB

def displayNames(names):
    for index in range(10):
       if names[index]:
            print(index+1, names[index])
    #next index
#end procedure

#main program
#initialise list to 10 blank spaces
names = [""]*10
choice = 0

while choice != 3:
    choice = displayMenu()
    if choice == 1:
        addName(names)
    elif choice == 2:
        displayNames(names)
 
print ("\nProgram terminating")

input("\nPress Enter to end ") 
