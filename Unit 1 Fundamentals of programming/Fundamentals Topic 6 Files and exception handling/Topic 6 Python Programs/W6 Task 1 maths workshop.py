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



#subroutine to calculate and display average mark
def calculateAverage():
    #now read the file one record at a time
    
    testResultsFile = open("studentNamesfile.txt","r")
    markRec = testResultsFile.readline()  
    field = markRec.split(",")
    numRecs = 0
    total = 0
    #   field[0] will be an empty string when end of file is reached
    while field[0] != '':       
        total = total + int(field[1])
        numRecs = numRecs + 1
        markRec = testResultsFile.readline()  
        field = markRec.split(",")
    average = total/numRecs
    print("\nAverage mark:", average)

#subroutine to display data
def displayData():
    #now read the file one record at a time
    
    testResultsFile = open("studentNamesfile.txt","r")
    markRec = testResultsFile.readline()  
    field = markRec.split(",")
    
    while field[0]!='': 
        studentName = field[0]
        result = field[1]
        print(studentName,result)
        markRec = testResultsFile.readline()  
        field = markRec.split(",")        
#endsub
    
    
#************************ main program **********************
option = displayMenu()

while option !="5":
    if option == "1":
        saveToFile("w")
    elif option == "2":
        saveToFile("a")
    elif option == "3":        
        calculateAverage()
    elif option == "4":        
        displayData()
    option = displayMenu()
#endwhile
print("You have chosen to quit the program")    

