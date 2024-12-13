print("Coding a Rainbow")
sentence = input("What sentence do you want rainbow-ising?\n")
# Defining a variable to store the color codes
red = ["r"]
blue = ['b', 'g', 'p', 'y']
green = ['g']
yellow = ['y']
purple = ['p']
orange = ['o']

for letter in sentence:
  if letter.lower() in red:
    print("\033[31m", end="")

  elif letter.lower() in blue:
    print("\033[34m", end="")

  elif letter.lower() in green:
    print("\033[32m", end="")

  elif letter.lower() in yellow:
    print("\033[33m", end="")

  elif letter.lower() in purple:
    print("\033[35m", end="")

  elif letter.lower() in orange:
    print("\033[33m", end="")

  elif letter.lower() == " ":
    print("\033[0m", end="")
  
  print(letter, end="")
  print('\033[0m', end='') #back to default
