symptom = ["YES"]
print("Do you have a temperature? (y or n) ", end="")
#convert to uppercase
symptom = input().upper()

# get the first character
symptom = symptom[0:1]

print("Test print... first character of response ",symptom)
if symptom == "Y":
    symptom = input("Is your throat sore? (y or n) ").upper()
    symptom = symptom[0:1]
    if symptom == "Y":
        print("You may have a throat infection...")
    else:
        print("You have a fever")
else:
    symptom = input("Do you have a cough? ")
    symptom = symptom.upper()
    symptom = symptom[0:1]

    if symptom == "Y":
        print("You may have a chest infection...")
    else:
        print("Sorry, your symptoms are extremely rare")
        print("We have no diagnosis")
input("Press Enter to end")
    
