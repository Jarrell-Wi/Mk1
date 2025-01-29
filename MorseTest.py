Number = 0
while Number < 1 or Number > 10:
    Number = int(input('Enter a whole positive number: '))
    if Number > 10:
        print('Number too large')
    elif Number < 1:
        print('Not a positive number.')
c = 1
for i in range(Number):
    print(c)
    c = (c * (Number - 1 - i)) // (i + 1)