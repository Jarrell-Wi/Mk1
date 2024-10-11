#AS AQA unit 1 H3 Q2 Password
password = input("Please enter password: ")
attempts = 1
while password != "Tues1212" and attempts<3:
    password = input("Password incorrect - please re-enter: ")
    attempts+=1
if password == "Tues1212":
    print("password accepted")
else:
    print("password rejected")
carryOn = input("Press Enter to continue")
