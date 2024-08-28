from getpass import getpass as input

print("----- Paper, Scissors, Rock -----")
print("In this game, you have to select your move (R, P or S)")

player1 = input("Player 1 > ").capitalize()
player2 = input("Player 2 > ").capitalize()

if player1 == "R":
  if player2 == "R":
    print("It's a tie!")
  elif player2 == "P":
    print("Player 2 wins!")
  elif player2 == "S":
    print("Player 1 wins!")
  else:
    print("Invalid move, Player 2! You have to select R, P or S")
elif player1 == "P":
  if player2 == "R":
    print("Player 1 wins!")
  elif player2 == "P":
    print("It's a tie!")
  elif player2 == "S":
    print("Player 2 wins!")
  else:
    print("Invalid move, Player 2! You have to select R, P or S")
elif player1 == "S":
  if player2 == "R":
    print("Player 2 wins!")
  elif player2 == "P":
    print("Player 1 wins!")
  elif player2 == "S":
    print("It's a tie!")
  else:
    print("Invalid move, Player 2! You have to select R, P or S")
else:
  print("Invalid move, Player 1! You have to select R, P or S")
  

