def game():
  mokeInfo = {} #Empty dictionary

  print("👾 MokéBeast - The Non-Copyright Generic Beast Battle Game 👾\n")
  mokeInfo["name"] = input("Input your beast's name > ")
  mokeInfo["type"] = input("Input your beast's type > ")
  mokeInfo["specialMove"] = input("Input your beast's special move > ")
  mokeInfo["hp"] = input("Input your beast's starting HP > ")
  mokeInfo["mp"] = input("Input your beast's starting MP > ")

  # Conditional to change colors based on type
  for value in mokeInfo.values():
    if mokeInfo["type"].lower() == "fire":
      print("\033[31m", end="")
    elif mokeInfo["type"].lower() == "water":
      print("\033[34m", end="")
    elif mokeInfo["type"].lower() == "air":
      print("\033[37m", end="")
    elif mokeInfo["type"].lower() == "earth":
      print("\033[32m", end="")
    else:
      print("\033[37m", end="")

  # Printing phrases based on type
  print(f"Your beast is called {mokeInfo['name']}. It is an {mokeInfo['type']} beast with a special move of {mokeInfo['specialMove']}.")

  # Restauraing colors
  print("\033[0m", end="")
  
  return mokeInfo

# Print dictionary
mokeGame = game()