#AQA  AS PP1 surname and initial
# accepts a string like Fred Jones and prints out Jones F
fullName = input ("Enter first name and surname separated by space: ")

#split into two strings using the separator " " i'e' space
splitString = fullName.split(" ")
surname = splitString[1]
firstName = splitString[0]
initial = firstName[0]
print(surname,initial)
