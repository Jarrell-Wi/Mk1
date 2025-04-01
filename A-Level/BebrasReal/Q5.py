# 2m takes 2 posts 2 railings 16 pickets
Length = 0
Stuff = input()
Stuff = Stuff.split(' ')
Posts = int(Stuff[0])
Railings = int(Stuff[1])
Pickets = int(Stuff[2])
Out = False
if Posts == 1:
    Out = True
while not Out:
    if Posts - 1 < 0:
        Out = True
        break
    else:
        Posts -= 1
    if Railings - 2 < 0:
        Out = True 
        break
    else:
        Railings -= 2
    if Pickets - 8 < 0:
        Out = True
        break
    else:
        Length += 2
        Pickets -= 8
print(Length)