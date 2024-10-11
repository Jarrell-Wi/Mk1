#AQA AS W1 Q1 Paint litres needed
height = float(input("Enter height of room in metres: "))
length = float(input("Enter length of room in metres: "))
width = float(input("Enter width of room in metres: "))
unpaintedSpaceArea = float(input("Enter area of unpainted space: "))
numCoats = int(input("Enter number of coats of paint required: "))
area = height * (length + width) * 2
print("Area",area)
paintArea = (area - unpaintedSpaceArea)     
print("paintArea", paintArea)
totalPaintArea = paintArea * numCoats
print ("Total paint area",totalPaintArea)
litresNeeded = round(totalPaintArea/11,2)              # assume 1 litre covers 11 sq m
print("You will need ",litresNeeded," litres")
