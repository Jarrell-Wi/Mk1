#AS AQA unit 1 W2 Q3 Online bookstore
import math
orderVal = float(input("Enter order value: "))
postageCharge = 5.0
print("Do you want to pay £5.00 for next day delivery? ")
postageCode = input("Enter 1 for next day delivery, 2 for 2nd class post: ")
if orderVal >=15.0 and postageCode == "2":
    postageCharge = 0
elif orderVal < 15.0 and postageCode == "2":
    postageCharge = 3.50

totalCharge = orderVal + postageCharge
#You can round to 2 decimal places but this will print 25.40 as 25.4
#totalCharge = round(totalCharge,2)

#To print currency amounts to two decimal places, you can put "markers" %0.2f
# into the string to mark the positions where 2 float values are to be inserted
#Follow the string with % (postageCharge,totalCharge) to show
#where the two float values are to be inserted
#see http://learning.londonmet.ac.uk/computing/cc0002n/webpages/chpt3_3.htm
print ("Postage charge: £%0.2f      Total charge  £%0.2f" % (postageCharge,totalCharge))

input("\nPress Enter to exit program ")
