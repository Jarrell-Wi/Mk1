Vowels = ['a', 'e', 'i', 'o', 'u']
Text = input()
if Text[0].lower() in Vowels:
    print(f'{Text}-yay')
else:
    Stored = Text[0]
    print(f'{Text[1:]}-{Stored}ay')
