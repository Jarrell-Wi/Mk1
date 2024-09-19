#AQA PP Try...Except example

names = ["Belinda", "Gerri", "Tom"]

for index in range(1,6):
    try:
        print(names[index])
    except:
        print("No more names in the array!")

print("Program continuing...")

fileFound = False
try:
    testFile = open ("testfile.txt","r")
except:
    print ("\n\nCannot find the file ... ending program\n")
    
else:    
    print ("Carry on...")
    fileFound = True

if fileFound == True:
    print("File opened")
    testFile.close()

