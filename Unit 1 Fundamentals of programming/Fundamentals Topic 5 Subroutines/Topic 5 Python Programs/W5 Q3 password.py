#AS AQA unit 1 W5 Q3 password

def getPword(attempt):
    pword = ""
    while len(pword)<5 or len(pword)>8:
        if attempt == 1:
            print("enter password:")
        else:
            print("enter password again:")
        pword = input()
        if len(pword)<5 or len(pword)>8:
            print("Error.  Password must be 6 to 8 characters long")
    return pword

#main program
pword1 = getPword(1)
pword2 = getPword(2)
while pword1 != pword2:
    print("Error - passwords do not match")
    pword1 = getPword(1)
    pword2 = getPword(2)      
print("Password change successful")
