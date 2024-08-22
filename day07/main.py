tvShow = input("What is your favorite tv show? ")
if tvShow == "the office":
  print("Ugh, why?")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter == "Dwigth":
    print("Right answer")
  elif faveCharacter == "Jim":
    print("Jim is the best")
  else:
    print("Nah, you're probably from HR")
elif tvShow == "supernatural":
  print("Aww, it's nice too")
  faveBrother = input("Who is your favorite brother? ")
  if faveBrother == "Sam":
    print("Sam is really sweet")
  else:
    print("I guess that's cool too")
else:
  print("Yeah, that's cool and all…")