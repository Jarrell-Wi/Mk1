#AS AQA unit 1 W4 Q4 Large Sales array



outletSales=[]
total = [0,0,0,0]

x = 0
#initialise outletSales with some values...
for quarter in range(4):
    x = x + 10
    outletSales.append([])  #append a new row to the 2-D array
    for n in range(50):
        outletSales[quarter].append(n+x)
    print ("Outlet, quarter, n", outletSales[quarter])
input("\nPress enter to print totals")

#now add up the sales for each quarter and print totals       
for quarter in range(4):
    for outlet in range(50):
        total[quarter] = total[quarter] + outletSales[quarter][outlet]  
    print("Total for quarter ",quarter+1, total[quarter])

input("\nPress Enter to end ")