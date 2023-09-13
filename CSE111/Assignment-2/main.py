#ClassWork
#task 1
def BMI(a, b):
    bmi = int(b)/((int(a)/100)**2)
    if bmi < 18.5:
        print("Score is {:.1f} You are Underweight".format(bmi))
    elif 18.5 <= bmi <= 24.9:
        print("Score is {:.1f} You are Normal".format(bmi))
    if 25 <= bmi <= 30:
        print("Score is {:.1f} You are Overweight".format(bmi))
    if bmi > 30:
        print("Score is {:.1f} You are obese".format(bmi))


user = input()
user1 = input()
BMI(user, user1)

#task 2
def Calc(item,place="Mohakhali"):
    sum=0
    if item.lower() == "bbq chicken cheese burger":
        sum += 250
    elif item.lower() == "beef burger":
        sum += 170
    elif item.lower() == "naga drums":
        sum += 200
    if place.lower() == "mohakhali":
        delivery_charge = 40
    else:
        delivery_charge = 60
    tax= (sum*8)/100
    Total_Price = sum + delivery_charge + tax
    print(Total_Price)
Calc("Beef burger", place="Dhanmondi")

#task 3
def Domain(check, new_domain, old_domain="kaaj.com"):
    old_email=check
    check=check.split("@")
    if check[1] != "new_domain":
        check[1] = new_domain

    new_email = check[0] + "@" + check[1]
    if new_email != old_email:
        print("Changed: ",new_email)
    else:
        print("Unchanged: ",new_email)

Domain("alice@kaaj.com" ,"sheba.xyz","kaaj.com")

#task 4
def function(a) :
  out = ''
  for i in a :
    if 97<=ord(i)<= 122 :
      out += i
  out1 = out[-1::-1]
  if out1 == out :
    return "palindrome"
  else :
    return "not palindrome"
v1 = input()
store = function(v1)
print(store)
#task 5
def fukU(days):
    year=days//365
    user=days%365
    months=user//30
    days=user%30
    print(year,"years", months, "months and", days, "days")
user=int(input())
fukU(user)

#task 6
def cap(pera):
    capitalized = ""
    if pera != "":
        if "a" <= pera[0] <= "z" and "a" <= pera[1] <= "z" or "A" <= pera[1] <= "Z":
            capitalized = pera[0].upper()+pera[1].lower()
        else:
            capitalized = pera[0]

        for i in range(2, len(pera)):
            if pera[i-1] == " " and pera[i] == "i" and pera[i+1] == " ":
                capitalized += "I"
            elif pera[i-2] == "?" or pera[i-2] == "." or pera[i-2] == "!":
                capitalized += pera[i].upper()
            else:
                capitalized += pera[i].lower()
        print(capitalized)
    else:
        print("Please enter a valid string.")


cap("my favourite animal is a dog. a dog has sharp teeth so that it can eat flesh very easily. do you know my pet dog’s name? i love my pet very much.")


#HomeWork

from IPython.display import clear_output
import time
#All the variables needed
board = [[1,2,3],[4,5,6],[7,8,9]] #The players will be placing their characters in this list
#and the whole game be conducted based on the current status of this list.
current_player_char = 'X' #The character of the current player
next_player_char = 'O' # The character of the next player
totalInputs = 9 #Since there are 9 slots in total in the whole board.
winner = None

def checkHorizontal():
  for i in range(len(board)):
      if board[i][0] == board[i][1] == board[i][2]:
        return True
      else:
        return False


def checkVertical():
  for i in range(0,1):
    for j in range(len(board)):
      if board[i][j] == board[i+1][j] == board[i+2][j]:
        return True
      else:
        return False

def checkDiagonal():
      if board[0][0] == board[1][1] == board[2][2] or board[0][2] == board[1][1]==board[2][0]:
        return True
      else:
        return False

def checkBoard():
  if checkHorizontal() or checkVertical() or checkDiagonal() is True:
    return True
  else:
    return False


def placeCharacterOnBoard(pos):
  global board
  if 1 <= pos <= 9:
    for i in range(len(board)):
      for j in range(len(board)):
        if board[i][j] == pos and board[i][j] !='X' and board[i][j] != 'O':
          board[i][j] = current_player_char
          return 1
  return 0

#This function prints the current status of the 'board' list in particular format.
def printCurrentBoard():
  print("-------------")
  for eachRow in board:
    print("|",end="")
    for eachCol in eachRow:
      print(f" {eachCol} ",end="|")
    print() #To move to the next row
    print("-------------")

#This function will be simulating the whole game.
def runGame():
  global current_player_char
  global next_player_char
  global winner
  welcome_msg = '''Welcome to the TIC-TAC-TOE game. The first player to place character on the board will be Player 1(Character X) and the other player will be Player 2(Character O).'''
  print(welcome_msg)
  inputCount= 0 #This variable is for counting the number of inputs and controlling the loop based on it.
  while inputCount < totalInputs:
    printCurrentBoard() #This function prints the current state of the board as a player needs to see it before making the next move.
    position = int(input(f"Player {(inputCount%2)+1},enter a position that does not contain any X or O:")) #The user needs to enter a position that does contain any X or O.
    validityofInput = placeCharacterOnBoard(position) #validityofInput will be 1 if the user inputs a valid "position"; otherwise it will be 0.
    inputCount+= validityofInput # If the inputs a valid "position", the inputCount will increase by one; otherwise it will remain as it is.
    if inputCount>=5: #There is no need to check the board before 5 valid inputs as there will be no winners before 5 valid inputs.
      if checkBoard(): #If checkBoard() returned True then current player won the game.
        winner = "Player 1" if current_player_char == 'X' else "Player 2"
        clear_output() #This function clears the output panel.
        break
    if validityofInput: #Only if the player inputs a valid "position", the player characters will be swapped for the next move.
      current_player_char,next_player_char = next_player_char,current_player_char #The players will place characters alternatively. So if X is the current player's character, in the next turn O will be the current player's character.
    clear_output() #This function clears the output panel before printing the current board status for the next player.
  printCurrentBoard()
  #After the while loop if the value of  winner is still none, that means the game ended in a draw; otherwise we have a winner.
  if winner != None:
    print(f"Well done, {winner}. You have won the game.")
  else:
    print(f"The game ended in a draw")


runGame()