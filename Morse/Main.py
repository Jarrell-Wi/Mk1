# Skeleton Program for the AQA AS Summer 2018 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS Programmer Team
# developed in a Python 3 environment


# Version Number : 1.6

SPACE = ' '
EOL = '#'
EMPTYSTRING = ''
FULLSTOP = '.'

def ReportError(s):
  print('{0:<5}'.format('*'),s,'{0:>5}'.format('*')) 
        
def StripLeadingSpaces(Transmission): 
  TransmissionLength = len(Transmission)
  if TransmissionLength > 0:
    FirstSignal = Transmission[0]
    while FirstSignal == SPACE and TransmissionLength > 0:
      TransmissionLength -= 1
      Transmission = Transmission[1:]
      if TransmissionLength > 0:
        FirstSignal = Transmission[0]
  if TransmissionLength == 0:
    ReportError("No signal received")
  return Transmission

def StripTrailingSpaces(Transmission): 
  LastChar = len(Transmission) - 1
  while Transmission[LastChar] == SPACE:
    LastChar -= 1
    Transmission = Transmission[:-1]
  return Transmission  

def GetTransmission():
  FileName = input("Enter file name: ")
  if '.txt' not in FileName:
    FileName += '.txt'
  try:
    FileHandle = open(FileName, 'r')
    Transmission = FileHandle.readline()
    FileHandle.close()
    Transmission = StripLeadingSpaces(Transmission)
    if len(Transmission) > 0:
      Transmission = StripTrailingSpaces(Transmission)
      Transmission = Transmission + EOL
  except:
    ReportError("No transmission found")
    Transmission = EMPTYSTRING
  return Transmission

def GetNextSymbol(i, Transmission):
  if Transmission[i] == EOL:
    print()
    print("End of transmission")
    Symbol = EMPTYSTRING
  else:
    SymbolLength = 0
    Signal = Transmission[i]
    while Signal != SPACE and Signal != EOL:
      i += 1
      Signal = Transmission[i]
      SymbolLength += 1
    if SymbolLength == 1:
      Symbol = '.'
    elif SymbolLength == 3:
      Symbol = '-'
    elif SymbolLength == 0: 
      Symbol = SPACE
    else:
      ReportError("Non-standard symbol received") 
      Symbol = EMPTYSTRING
  return i, Symbol 

def GetNextLetter(i, Transmission):
  SymbolString = EMPTYSTRING
  LetterEnd = False
  while not LetterEnd:
    i, Symbol = GetNextSymbol(i, Transmission)
    if Symbol == SPACE:
      LetterEnd = True
      i += 4
    elif Transmission[i] == EOL:
      LetterEnd = True
    elif Transmission[i + 1] == SPACE and Transmission[i + 2] == SPACE:
      LetterEnd = True
      i += 3
    else:
      i += 1
    SymbolString = SymbolString + Symbol
  return i, SymbolString

def Decode(CodedLetter, Dash, Letter, Dot, Codes):
  Exists = False
  if CodedLetter in Codes:
    Exists = True
  else:
    print('Invalid symbol recieved')
    return '*'
  CodedLetterLength = len(CodedLetter)
  Pointer = 0
  for i in range(CodedLetterLength):
    Symbol = CodedLetter[i]
    if Symbol == SPACE:
      return SPACE
    elif Symbol == '-':
      Pointer = Dash[Pointer]
    else:
      Pointer = Dot[Pointer]
  return Letter[Pointer]

def ReceiveMorseCode(Dash, Letter, Dot, Codes): 
  PlainText = EMPTYSTRING
  MorseCodeString = EMPTYSTRING
  Transmission = GetTransmission() 
  LastChar = len(Transmission) - 1
  i = 0
  while i < LastChar:
    i, CodedLetter = GetNextLetter(i, Transmission)
    MorseCodeString = MorseCodeString + SPACE + CodedLetter
    PlainTextLetter = Decode(CodedLetter, Dash, Letter, Dot, Codes)
    PlainText = PlainText + PlainTextLetter
  print(MorseCodeString)
  print(PlainText)

def SendMorseCode(MorseCode):
  Quaternary = ''
  PlainText = input("Enter your message (uppercase letters and spaces only): ")
  PlainTextLength = len(PlainText)
  MorseCodeString = EMPTYSTRING
  for i in range(PlainTextLength):
    PlainTextLetter = PlainText[i]
    if PlainTextLetter == SPACE:
      Index = 0
    elif PlainTextLetter == FULLSTOP:
        Index = 27
    else: 
      Index = ord(PlainTextLetter) - ord('A') + 1
    CodedLetter = MorseCode[Index]
    for i in CodedLetter:
      if i == '-':
        Quaternary += '3'
      elif i == '.':
        Quaternary += '2'
      elif i == ' ':
        Quaternary += '1'
    
    Quaternary += '0'
    MorseCodeString = MorseCodeString + CodedLetter + SPACE

  return MorseCodeString, Quaternary

def DisplayMenu():
  print()
  print("Main Menu")
  print("=========")
  print("R - Receive Morse code")
  print("S - Send Morse code")
  print('P - Print Morse code symbols')
  print('T - Transmit Morse code')
  print('C - Convert Morse code')
  print('E - Send encrpted message')
  print("X - Exit program")
  print()

def GetMenuOption():
  choices = ['R', 'S', 'X', 'T', 'C', 'E']
  MenuOption = EMPTYSTRING
  while len(MenuOption) != 1:
    MenuOption = input("Enter your choice: ")
    MenuOption = MenuOption.upper()
    if MenuOption not in choices:
        print('Invalid choice, please choose a letter from the menu: ')
  return MenuOption

def ConvertMorseCode(MorseCode, Letters):
  Result = ''
  Morse = input('Enter Morse code: ')
  Morse = Morse.split(' ')
  for i in Morse:
    if i in MorseCode:
      Result += Letters[MorseCode.index(i)]
    else:
      Result += '*'
      print('Invalid Symbol entered')
  print(Result)

def SendSignals()

def TransmitMorseCode(Codes):
  data = ''
  code = SendMorseCode(Codes)
  for i in code:
    if i == '.':
      data += '= '
    elif i == '-':
      data += '=== '
    else:
      data += '  '
    
  name = input('Enter filename to write to: ')
  with open(name,'w+') as file:
    file.write(data)
    file.close()

def PrintSymbols(Letters, Codes):
  for i in range(len(Letters)):
    print(f'{Letters[i]} | {Codes[i]}')
  return

def SendEncryptedMorse(MorseCode):
  PlainText = input("Enter your message (uppercase letters and spaces only): ")
  Shift = int(input('Enter Ceasar shift: '))
  PlainTextLength = len(PlainText)
  MorseCodeString = EMPTYSTRING
  for i in range(PlainTextLength):
    PlainTextLetter = PlainText[i]
    PlainTextLetter = ord(PlainTextLetter) + Shift
    if PlainTextLetter == SPACE:
      Index = 0
    elif PlainTextLetter == FULLSTOP:
     Index = 27
    else: 
      Index = ord(PlainTextLetter) - ord('A') + 1
    CodedLetter = MorseCode[Index]

    MorseCodeString = MorseCodeString + CodedLetter + SPACE

  return MorseCodeString


def SendReceiveMessages():
  Dash = [20,23,27,0,24,1,0,17,0,21,0,25,0,15,11,0,0,0,2,22,13,0,0,10,0,0,0]
  Dot = [5,18,2,0,2,9,0,26,0,19,0,3,0,7,4,0,0,0,12,8,14,6,0,16,0,0,0]
  Letter = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','.']

  MorseCode = [' ','.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.-.-.-']

  ProgramEnd = False
  while not ProgramEnd:
    DisplayMenu() 
    MenuOption = GetMenuOption()
    if MenuOption == 'R':
      ReceiveMorseCode(Dash, Letter, Dot, MorseCode)
      
    elif MenuOption == 'S':
      Codes = (SendMorseCode(MorseCode))
      print(Codes[0])
      print(Codes[1])
      
    elif MenuOption == 'P':
      PrintSymbols(Letter[1::], MorseCode[1::])
      
    elif MenuOption == 'T':
      TransmitMorseCode(MorseCode)
    
    elif MenuOption == 'C':
      ConvertMorseCode( MorseCode, Letter)
    
    elif MenuOption == 'E':
      print(SendEncryptedMorse(MorseCode))

    elif MenuOption == 'X':
      ProgramEnd = True
    

if __name__ == "__main__":
  SendReceiveMessages()
