def encrypt(Phrase, Shift):
    Final = ''
    for i in Phrase:
        Final = Final + chr(ord(i)+ Shift)
    return(Final)

def decrypt(Phrase, Shift):
    Final = ''
    for i in Phrase:
        Final = Final + chr(ord(i)- Shift)
    return(Final)

a = input('>')
b = int(input('>'))
c = input('Encrypt or Decrypt E/D: ')
if c == 'E':
    print(encrypt(a, b))
else:
    print(decrypt(a, b))