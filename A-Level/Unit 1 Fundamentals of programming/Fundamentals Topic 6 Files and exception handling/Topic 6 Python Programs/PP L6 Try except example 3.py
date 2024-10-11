#AQA AS PP Try except example 3
ageValid = False
age = 0

while age < 11 or age > 18:
    age = input("Enter age between 11 and 18: ")
    try:
        age = int(age)
    except:
        print("Please enter an integer")
        age = 0

print ("You entered an age of ",age)        
