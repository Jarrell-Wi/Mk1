a = float(input('Order price'))
if a >= 15.00:
    b = input('Do you want next day delivery?').upper()
    if b == 'Yes':
        a += 5
        print(a)
else:
    b = input('Do you want next day delivery?').upper()
    if b == 'Yes':
        a += 5
    else:
        a += 3.5
print(a)