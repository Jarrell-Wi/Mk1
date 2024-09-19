#AS AQA unit 1 W2 Q7 car rental
print("Enter a choice of:")
print("    1 Economy car")
print("    2 Saloon car")
print("    3 Sports car")
selection1 = int(input("Choice: "))
choice = "valid"
if selection1 == 1:
    print("You chose Economy car")
elif selection1 == 2:
    print("You chose Saloon car")
elif selection1 == 3:
    print("You chose Sports car")
else:
    print("Invalid choice")
    choice = "invalid"
 

if choice=="valid":
    selection2 = input("Do you wish to proceed (P) or cancel (C)? ")
    selection2 = selection2.upper()
    selection2FirstLetter = selection2[0]
    if selection2FirstLetter == "P":
        print("You chose to proceed")
    elif selection2FirstLetter =="C":
        print("You chose to cancel")
    else:
        print("Invalid entry")
    print("Have a nice day")
input("\nPresss Enter to exit")
           
