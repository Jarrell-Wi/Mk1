#AS AQA unit 1 W3 Q3 part numbers

oldModel = 0
total = 0
partnum = input("Enter part number: ")
while partnum != "9999":
    while len(partnum) !=4:
        partnum = input("Error: enter 4-digit number: ")
    if partnum[3] >= "6" and partnum[3]<="8":
        oldModel += 1
        print(partnum[3], oldModel)
    total += 1
    partnum = input("Enter part number: ")
#endwhile
print("Number of old models:", oldModel)
print("Total number of parts:", total)
