#AS AQA unit 1 W2 Q4 Decision table
mark = int(input("Enter exam mark %: "))
attendance = int(input ("Enter attendance %: " ))
if attendance > 90:
    if mark > 90:
        print ("Grade A")
    elif mark >80:
        print ("Grade B")
    elif mark >70:
        print ("Grade C")
    else:
        print("fail")
else:
    print("fail")

input("\nPress Enter to exit program ")