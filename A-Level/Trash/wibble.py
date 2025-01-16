def wibbler(n):
    if (n > 0):
        print('wibble')
        return wibbler(n-1)
wibbler(100)
 