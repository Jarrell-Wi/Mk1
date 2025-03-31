Runners = int(input())
Happy = 0
for i in range(Runners):
    ctr = 0
    prev = 0
    Athlete = input()
    Stats = Athlete.split(' ')
    for i in Stats:
        if int(i) > prev:
            ctr += 1
        prev = int(i)
    if ctr == 5:
        Happy += 1
print(Happy)