def Big(a,b,c):
    set = [a, b, c]
    set.sort()
    return(set[len(set) - 1])

a = int(input('>'))
b = int(input('>'))
c = int(input('>'))
print(Big(a,b,c))