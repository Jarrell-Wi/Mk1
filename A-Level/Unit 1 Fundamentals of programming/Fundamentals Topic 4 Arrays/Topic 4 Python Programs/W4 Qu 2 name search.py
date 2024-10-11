# Worksheet 4 Task 1 Qu 2 name search
max = 6
name = ["Annie","Bob","Charles","Dan","Erica","Faisal"]
print("Enter search name: ")
searchName = input()
found = False
for index in range(max):
    if name[index] == searchName:
        print("record number ", index+1)
        found = True
if found == False:
    print("Search name not found")
    
input("\nPress Enter to end ")