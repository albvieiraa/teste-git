import random

# Function to generate a random number (bingo)
def generateBingo():
  randomNum = random.sample(range(1,91),8)
  randomNum.sort()
  randomNum.insert(4, "BINGO")

  bingoCard = [randomNum[i:i+3] for i in range(0, len(randomNum), 3)]
  return bingoCard

# Display the bingo card
def displayCard(card):
  print("David's Nan's Bingo Card Generator")
  print("-" * 17)
  for row in card:
      print(" | ".join(f"{str(x):^3}" for x in row))
      print("-" * 17)

bingoCard = generateBingo()
displayCard(bingoCard)