#AS AQA unit 1 W6 Q1 write to file
# program displays menu of options to
#input, save and print results from maths test

#subroutine to display menu and validate choice
def displayMenu():
   #display menu of options      
    print("\n1. Input data and save to new file")
    print("2. Input data and append to existing file")
    print("3. Calculate and display average mark")
    print("4. Display data")
    print("5. Quit\n")
    choice = input("Enter your choice: ")
    while choice < '1' or choice > '5':
        choice = input ("Invalid choice - please re-enter: ") 
    return choice  


#subroutine to input data and save to a new file 
def saveToFile(openMode):
    testResultsFile = open("studentNamesfile.txt",openMode)
    print("\nEntering sub saveToFile")
    studentMark = "0"
    studentName = input ("Enter a student name, xxx to finish : ")
    while studentName != "xxx":
        studentMark = (input ("Enter mark : "))
        testResultsFile.write(studentName+","+ studentMark+"\n")
        studentName = input ("Enter a student name, xxx to finish : ")    
    testResultsFile.close


#subroutine to read from text file into array
def readIntoArray():
    name = []
    mark = []
    #now read the file one record at a time
    print("Now read the file one record at a time")
    testResultsFile = open("studentNamesfile.txt","r")
    markRec = testResultsFile.readline()  
    field = markRec.split(",")

    #   field[0] will be an empty string when end of file is reached
    while field[0]!='':       
    #put the data into two arrays
        name.append(field[0])
        mark.append(field[1])
        markRec = testResultsFile.readline()  
        field = markRec.split(",")
    testResultsFile.close()
    return name,mark

#subroutine to calculate and display average mark
def calculateAverage(result):
    total = 0
    numRecs = len(result)
    for n in range(numRecs):
        total = total + int(result[n])
    average = total/numRecs
    print("\nAverage mark:", average)

#subroutine to display data held in array
def displayData(studentName,result):
    numRecs = len(studentName)
    for n in range(numRecs):
        print(studentName[n],result[n])
#endsub
    
    
#main program
option = displayMenu()

while option !="5":
    if option == "1":
        saveToFile("w")
    elif option == "2":
        saveToFile("a")
    elif option == "3":
        name,mark = readIntoArray()
        calculateAverage(mark)
    elif option == "4":
        name,mark = readIntoArray()
        displayData(name,mark)
    option = displayMenu()
#endwhile
print("You have chosen to quit the program")    

