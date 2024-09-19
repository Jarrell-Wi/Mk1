#AQA AS H1 hundreds tens and units

print("Enter a three-digit number: ", end = " ")
threeDigitNumber = int(input())
hundreds = threeDigitNumber // 100       # // is DIV, integer division
tens = (threeDigitNumber % 100)//10      # % is MOD 
units = (threeDigitNumber % 100) % 10
print (hundreds,"hundreds ", end =" ")
print(tens,"tens",end = " ")
print("and ",units,"units")

input("\nPress Enter to exit program ")