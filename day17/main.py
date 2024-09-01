from getpass import getpass as input

print(f"{'=' * 5}E P I C    🪨  📄 ✂️    B A T T L E ")
print("In this game, you have to select your move (R, P or S)\n")

player1_score = 0
player2_score = 0

while True:
  player1 = input("Player 1 > ").capitalize()
  player2 = input("Player 2 > ").capitalize()

  if player1 == "R":
    if player2 == "R":
      print("It's a tie!")
    elif player2 == "S":
      print("Player 1 wins! Rock smashes Scissors!")
      player1_score += 1
    elif player2 == "P":
      print("Player 2 wins! Paper covers Rock!")
      player2_score += 2

  elif player1 == "P":
    if player2 == "P":
      print("It's a tie!")
    elif player2 == "R":
      print("Player 1 wins! Paper covers Rock!")
      player1_score += 1
    elif player2 == "S":
      print("Player 2 wins! Scissors cuts Paper!")
      player2_score += 1

  elif player1 == "S":
    if player2 == "S":
      print("It's a tie!")
    elif player2 == "P":
      print("Player 1 wins! Scissors cuts Paper!")
      player1_score += 1
    elif player2 == "R":
      print("Player 2 wins! Rock smashes Scissors!")
      player2_score += 1

  print(f"Player 1 has {player1_score} wins.")
  print(f"Player 2 has {player2_score} wins.")

  if player1_score == 3 or player2_score == 3:
    print("Thanks for playing!")
    exit()

  else:
    continue

