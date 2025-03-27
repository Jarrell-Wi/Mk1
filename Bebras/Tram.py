Passengers = input()
Passengers = Passengers.split(',')
Held = 0
for i in Passengers:
    j = i.split(' ')
    Held += int(j[0])
    Held -= int(j[1])
print(Held)