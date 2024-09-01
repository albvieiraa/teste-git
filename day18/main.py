import random

print("Guess the Number!\n")

random_number = random.randint(1, 101)
attempts = 0

while True:
  guess = int(input("Guess a number between 1 and 100: "))
  if guess < 1:
    print("Oh no! That's not a valid guess. Try again!")
  elif guess > random_number:
    print("Hmm... too high! Try it again \n")
    attempts += 1
  elif guess < random_number:
    print("Hmm... too low! Try it again \n")
    attempts +=1
    continue
  elif guess == random_number:
    print("Congratulations! You guessed the number!")
    break

  else:
    print("I didn't recognize this number. Try again")

  if attempts == 5:
    print(f"Sorry, you've run out of attempts. The number was {random_number}")
    exit()

