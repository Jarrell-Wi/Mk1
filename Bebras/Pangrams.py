letters = []
for i in range(26):
    letters.append(chr(i + 97))
Text = input()
for i in range(len(Text)):
    if Text[i].lower() in letters or Text[i].upper() in letters:
        letters.remove(Text[i].lower())
if len(letters) == 0:
    print('Pangram')
else:
    print('Not a pangram')