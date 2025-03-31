Held = 0
ctr = 0
Manage = input()
InOut = Manage.split(',')
for i in InOut:
    Passengers = i.split(' ')
    for i in range(int(Passengers[0])):
        if Held > 0:
            Held -= 1
    for i in range(int(Passengers[1])):
        Held += 1
        if Held > 8:
            ctr += 1
            Held -= 1
print(ctr)