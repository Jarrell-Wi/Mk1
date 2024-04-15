a = input('>')
ASCII = []
Binary = []
for i in range(len(a)):
    ASCII.append(ord(a[i]))
for i in range(len(ASCII)):
    Binary.append(bin(ASCII[i]))
for i in range(len(Binary)):
    Binary[i] = str(Binary[i])
    Binary[i][0] = ''
    Binary[i][1] = ''

    print(ASCII[i])
    print(Binary[i])
    