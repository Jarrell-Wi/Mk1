#Skeleton Program for the AQA AS1 Summer 2016 examination
#this code should be used in conjunction with the Preliminary Material
#written by the AQA AS1 Programmer Team
#developed in a Python 3 programming environment

#Version Number 1.0

import random
def Quit():
  print('Game Closing...')

def GetRowColumn():
  print()
  Column = int(input("Please enter column: "))
  Row = int(input("Please enter row: "))
  if Row < 0 or Row >= 10 or Column < 0 or Column >= 10:
    print('Invalid input Target is out of board range')
    Row, Column = GetRowColumn()
  print()
  return Row, Column

def MakePlayerMove(Board, Ships, torpedoes):
  torpedoes -= 1
  Row, Column = GetRowColumn()
  if Board[Row][Column] == "m" or Board[Row][Column] == "h":
    print("Sorry, you have already shot at the square (" + str(Column) + "," + str(Row) + "). Please try again.")
  elif Board[Row][Column] == "-":
    print("Sorry, (" + str(Column) + "," + str(Row) + ") is a miss.")
    Board[Row][Column] = "m"
  else:
    print("Hit at (" + str(Column) + "," + str(Row) + ").")
    Board[Row][Column] = "h"
  return(torpedoes)

def SetUpBoard():
  Board = []
  for Row in range(10):
    BoardRow = []
    for Column in range(10):
      BoardRow.append("-")
    Board.append(BoardRow)
  return Board

def LoadGame(Filename, Board):
  BoardFile = open(Filename, "r")
  for Row in range(10):
    Line = BoardFile.readline()
    for Column in range(10):
      Board[Row][Column] = Line[Column]
  BoardFile.close()

def SaveGame(Board):
  check = input('Do you want to save: ')
  if check == 'Y':
    filename = input('Enter Filename: ') + '.txt'
    file = open(filename, 'w')
    for Row in range(10):
      for Column in range(10):
        line = Board[Row][Column]
        file.write(line)
      file.write('\n')
  Choice = input('Do You Want To Quit: ')
  if Choice == 'Y':
    Quit()
  
  else:
    print()
    print('Game Continues')
             
def PlaceRandomShips(Board, Ships):
  for Ship in Ships:
    Valid = False
    while not Valid:
      Row = random.randint(0, 9)
      Column = random.randint(0, 9)
      HorV = random.randint(0, 1)
      if HorV == 0:
        Orientation = "v"
      else:
        Orientation = "h"
      Valid = ValidateBoatPosition(Board, Ship, Row, Column, Orientation)
    print("Computer placing the " + Ship[0])
    PlaceShip(Board, Ship, Row, Column, Orientation)

def PlaceShip(Board, Ship, Row, Column, Orientation):
  if Orientation == "v":
    for Scan in range(Ship[1]):
      Board[Row + Scan][Column] = Ship[0][0]
  elif Orientation == "h":
    for Scan in range(Ship[1]):
      Board[Row][Column + Scan] = Ship[0][0]

def ValidateBoatPosition(Board, Ship, Row, Column, Orientation):
  if Orientation == "v" and Row + Ship[1] > 10:
    return False
  elif Orientation == "h" and Column + Ship[1] > 10:
    return False
  else:
    if Orientation == "v":
      for Scan in range(Ship[1]):
        if Board[Row + Scan][Column] != "-":
          return False
    elif Orientation == "h":
      for Scan in range(Ship[1]):
        if Board[Row][Column + Scan] != "-":
          return False
  return True

def CheckWin(Board):
  for Row in range(10):
    for Column in range(10):
      if Board[Row][Column] in ["A","B","S","D","P"]:
        return False
  return True

def PrintBoard(Board):
  print()
  print("The board looks like this: ")
  print()
  print (" ", end="")
  for Column in range(10):
    print(" " + str(Column) + "  ", end="")
  print()
  for Row in range(10):
    print (str(Row) + " ", end="")
    for Column in range(10):
      if Board[Row][Column] == "-":
        print(" ", end="")
      elif Board[Row][Column] in ["A","B","S","D","P"]:
        print(" ", end="")
      else:
        print(Board[Row][Column], end="")
      if Column != 9:
        print(" | ", end="")
    print()

def DisplayMenu():
  print("MAIN MENU")
  print()
  print("1 - Start new game")
  print("2 - Load training game")
  print('3 - Load Saved Game')
  print()
  print("9 - Quit")
  print()

def GetMainMenuChoice():
  print("Please enter your choice: ", end="")
  Choice = int(input())
  print()
  return Choice

def PlayGame(Board, Ships):
  torpedoes = 20
  GameWon = False
  while not GameWon:
    PrintBoard(Board)
    print('You have', torpedoes,'torpedoes.')
    torpedoes = MakePlayerMove(Board, Ships, torpedoes)
    GameWon = CheckWin(Board)
    SaveGame(Board)
    if GameWon and torpedoes >= 0:
      print("All ships sunk!")
      print()
    elif torpedoes == 0:
      print('Game Over.')
      print('You ran out of torpedoes')
      break

if __name__ == "__main__":
  TRAININGGAME = "Training.txt"
  MenuOption = 0
  while not MenuOption == 9:
    Board = SetUpBoard()
    Ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Submarine", 3], ["Destroyer", 3], ["Patrol Boat", 2]]
    DisplayMenu()
    MenuOption = GetMainMenuChoice()
    if MenuOption == 1:
      PlaceRandomShips(Board, Ships)
      PlayGame(Board,Ships)
    if MenuOption == 2:
      LoadGame(TRAININGGAME, Board)
      PlayGame(Board, Ships)
    if MenuOption == 9:
      final = input('Are You Sure: ')
      if final == 'Y':
        Quit()
      else:
        MenuOption = 0