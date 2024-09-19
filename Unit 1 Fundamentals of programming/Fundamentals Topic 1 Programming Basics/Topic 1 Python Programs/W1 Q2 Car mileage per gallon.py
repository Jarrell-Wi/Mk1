#AQA AS W1 Q2 Car mileage per gallon

litresPerGallon = 4.546
previousCarMileage = float(input("Enter previous mileometer reading: "))
currentCarMileage = float(input("Enter current mileometer reading: "))
litresToFillTank = float(input("Enter litres needed to fill tank: "))
totalMiles = currentCarMileage - previousCarMileage
gallonsToFillTank = litresToFillTank / litresPerGallon
mileage = totalMiles /gallonsToFillTank
mileage = int(mileage)
print("Miles per gallon :", mileage)
