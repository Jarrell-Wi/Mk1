#AS AQA unit 1 W3 Q2 fever
temp = 0
hour = 0
total = 0
fever = 0
#while hour < 7:
while hour<6:
    temp = float(input("Enter temperature: "))
    if temp > 37:
        fever += 1
    total = total + temp
    hour+= 1
    print("Hour", hour,"Total of temperature readings", total," fever: ",fever)
#endwhile
average = round(total/hour,1)
print ("Average temperature:",average)
print("Incidents of fever:", fever)
