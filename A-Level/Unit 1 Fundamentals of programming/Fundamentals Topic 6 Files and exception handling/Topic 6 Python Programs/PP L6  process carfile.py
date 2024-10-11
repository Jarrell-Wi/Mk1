#AQA AS PP L6 write to and read from car file
#program to append data to a text file
#if the file does not exist, it will be created 

carFile = open("carFile.txt","a")
print("This program lets you enter records to a file called carFile.txt")
print("If the file doesn't exist, it will be created.")
carModel = input("Enter car model, xxx to end: ")
while carModel!="xxx": 
    carPrice = input("Enter price of car: ")    
    carFile.write(carModel+","+carPrice+"\n")
    carModel = input("Enter car model: ")

carFile.close()

carFile = open("carFile.txt", "r")
print("\nthe file has been closed and reopened for reading\n")
wholefile = carFile.read()
print(wholefile)   
carFile.close()

# Alternatively, you can read the file record by record
# and calculate the total value of all cars

carFile = open("carFile.txt", "r")
totalcarPrice = 0
carRec = carFile.readline()
field = carRec.split(",")
#field[0] will be empty when the end of file is reached
while field[0]!='':       
    print ("fields are:",field[0],",",field[1])
    carPrice = int(field[1])
    totalcarPrice = totalcarPrice + carPrice
    carRec = carFile.readline()
    field = carRec.split(",")
print("Total value of all cars £", totalcarPrice)

input("\n Press Enter to exit")   
    
