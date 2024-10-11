#AQA AS H6 School match scores

#subroutine to display menu
def menu():
    print("Select from the following options: \n")
    print("1 Enter and save new data")
    print("2 Load and display data")
    print("3 Quit")
    response = input("\nEnter your selection: ")
    while response<"1" or response >"3":
        response = input("Error... enter a number between 1 and 3: ")
        
    return response

#subroutine to enter new data
def getData(school, wins):
    for index in range(3):
       valid = False
       school[index]=input("Enter school: ")
       while not valid:
           try:
               wins[index] = input ("Enter wins: ")
               numwins = int(wins[index])    #test for integer
               while numwins < 0 or numwins>20:                  
                   wins[index] = input ("Error... re-enter wins: ")
                   numwins = int(wins[index])   #test for integer          
               valid = True
           except:
               print("Please enter an integer")
            #end except
        #endwhile
    #endfor
#endsub
               
#subroutine to save data to disk
def save(school, wins, filename):
    matchFile = open(filename,"w")
    for index in range(3):
       matchFile.write(school[index]+"," + wins[index] + "\n")
    print("\ndata saved\n")
    matchFile.close()

#subroutine to load records into an array and display data
def loadAndDisplay(school, wins,filename):
    matchFile = open(filename,"r")
    
    for index in range(3):
        schoolRec = matchFile.readline()
        field = schoolRec.split(",")
        school[index] = field[0]
        wins[index] = field[1]
        print ("School: ",school[index], "  Wins: ",wins[index])
    matchFile.close()



#************************* MAIN PROGRAM  ****************************               
school =["","",""]
wins = [0,0,0]
filename = "teamScores.txt"
choice = menu()
while choice >="1" and choice <="3":
    if choice == "1":
        getData(school,wins)
        save(school, wins, filename)
    elif choice == "2":
        loadAndDisplay(school, wins, filename)
    else:
        print("You have chosen to end the program")
        break   #exit while loop
    choice = menu()
    #endif
#endwhile
#end of program
