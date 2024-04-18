a = input('>')
ASCII = []
Binary = []
for i in range(len(a)):
    ASCII.append(ord(a[i]))
for i in range(len(ASCII)):
    Binary.append(bin(ASCII[i]))
for i in range(len(Binary)):
    Binary[i] = str(Binary[i])
print(ASCII)
print(Binary)