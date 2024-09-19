#AS AQA unit 1 W6 Q7 exception handling

fileName = input ("Please enter file name to record seat sales: ")
theatreFile = open(fileName,"a")

performanceDate = input("Enter performance date, ddmmyy (xxx to end): ")
while performanceDate!= "xxx":    
    validSeatsSold = False

    while not validSeatsSold:
        seatsSold = input("Enter seats sold: ")
        try:
           integerSeats = int(seatsSold)
           validSeatsSold = True
        except:
            print("Invalid entry ... please re-enter.")
    #endwhile      
        
    theatreFile.write(performanceDate +"," + seatsSold +"\n")          
    performanceDate = input("Enter performance date, ddmmyy (xxx to end): ") 
#endwhile
theatreFile.close

#***********************************************************************
#************************** Part 2 of program **************************
#***********************************************************************

#now reopen the file for reading
print("\nReading audience numbers...")
fileName = input ("Please enter file name to read seat sales: ")
try:
    theatreFile = open(fileName,"r")
    fileOpened = True
except:
    print("File not found ... program ending ")
    fileOpened = False

if fileOpened:
    seatsRec = theatreFile.readline()
    field = seatsRec.split(",")        
    while field[0]!='':
        print("Date: ", field[0],end=" ")
        print("Seats sold: ", field[1])
        seatsRec = theatreFile.readline()
        field = seatsRec.split(",")
     #endwhile
#endif
print("\nEnd of program\n")
              
              
          
