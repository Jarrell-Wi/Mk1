#AS AQA unit 1 H4 Q3 Medal array
school = ["AAAA", "BBBB","CCCC","DDDD"]
medal = [4,7,1,3]
schoolNumber = int(input("Enter school number, between 1 and 4: "))
while schoolNumber !=-1:
    while (schoolNumber <1 or schoolNumber >4) and schoolNumber!=-1:
#        schoolNumber = schoolNumber -1
        schoolNumber = int(input("Invalid number, please re-enter, -1 to end: "))      
    #endwhile
        medal[schoolNumber-1] +=1
        print(medal)
    schoolNumber = int(input("Enter school number, -1 to end: "))

#endwhile
for n in range(4):
    print("School number ",n+1, "   School name ",school[n], \
           "   Number of medals ",medal[n])
#end for

input("\nPress Enter to end ")