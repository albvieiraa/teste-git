print(f"{'=' * 10} GUESS THE ANIMAL SOUND {'=' * 10}")

exit = "no"

while exit == "no":
  animal = input("What animal do you want? ").lower()
  if animal == "cow":
    print("A cow goes moo.")
  elif animal == "dog":
    print("A dog goes woof.")
  elif animal == "cat":
    print("A cat goes meow.")
  elif animal == "sheep":
    print("A sheep goes baa.")
  else:
    print("Sorry, I don't know that animal.")

  exit = input("Do you want to exit? ").lower()