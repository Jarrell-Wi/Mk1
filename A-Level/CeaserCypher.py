def encrypt(Phrase, Shift):
    Final = ''
    for i in Phrase:
        Final = Final + chr(ord(i)+ Shift)
    return(Final)

def decrypt(Phrase, Shift):
    Final = ''
    for i in Phrase:
        set = []
        for j in Phrase:
            Final =''
            Final = Final + chr(ord(i)+ j)
            set.append(Final)
    
    return(set)

a = input('>')
b = int(input('>'))
c = input('Encrypt or Decrypt E/D: ')
if c == 'E':
    print(encrypt(a, b))
else:
    print(decrypt(a, b))