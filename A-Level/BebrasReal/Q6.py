Stack = input()
Stack = Stack.split(' ')
Stacks = []
for i in Stack:
    Stacks.append(int(i))
Days = 0
Done = False
while not Done:
    ctr = 0
    for i in range(len(Stacks)):
        if i != len(Stacks) - 1:
            if Stacks[i] > Stacks[i + 1]:
                Stacks[i+ 1] += 1
                Days += 1
            else:
                
                ctr += 1
    if ctr == len(Stacks):
        Done = True
    
print(Days)