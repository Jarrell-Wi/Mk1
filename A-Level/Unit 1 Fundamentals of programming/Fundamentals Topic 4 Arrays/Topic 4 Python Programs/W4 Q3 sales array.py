#AS AQA unit 1 W4 Q3 Sales array
outlet1Sales = [10,12,15,10]
outlet2Sales = [5,8,3,6]
outlet3Sales = [10,12,15,10]
total = [0,0,0,0]

for quarter in range(4):   
    total[quarter] = total[quarter] + outlet1Sales[quarter]+ \
                     outlet2Sales[quarter]+outlet3Sales[quarter]
                    #line break signified by \
#now print totals
    print("Total for quarter ",quarter+1, total[quarter])

input("\nPress Enter to end ")