import random

# function of the game
def hagman():
  listOfWords = ["apple", "orange", "grapes", "pear"]
  randomWord = random.choice(listOfWords)
  showWord = "_" * len(randomWord)
  chances = 6
  letterTaken = []

  print("🌟Hangman🌟")
  while chances > 0:
    # show the word
    print(f"\nWord: {showWord} ", end=" ")
    print(f"Chances left: {chances}")
    print(f"Letters taken: {letterTaken}")
    
    # ask the user to guess a letter
    letter = input("Choose a letter: ").lower()
    if letter in letterTaken:
      print("You've already tried that letter.")
      continue
    
    letterTaken.append(letter)
    # check if the letter is in the word
    if letter in randomWord:
      print("You found a letter!")
    else:
      print("Oh no, that letter is not in the word.")
      chances -= 1

    allLetters = True
    print()
    for i in randomWord:
      if i in letterTaken:
        print(i, end="")
      else:
        print("_", end="")
        allLetters = False
        print()

    if allLetters:
      print(f"\nYou won with {chances} left!")
      break

    if chances <= 0:
      print(f"You ran out of chances. The answer was {randomWord}.")
      break

if __name__ == "__main__":
  hagman()