import random

print("Guessing a number - Level Hard \nYou had only 5 chances to guess the number")

random_number = random.randint(1,1000000)
attempts = 0

while True:
  guess = int(input("Guess a number between 1 and 1,000,000: "))
  if guess < 0:
    print("You have entered a negative number. Exiting the game.")
    exit()
  elif guess > random_number:
    print("Too high, try it again.")
    attempts += 1
  elif guess < random_number:
    print("Too low, try it again.")
    attempts += 1
  elif guess == random_number:
    print(f"Congratulations! You guessed the number in {attempts} attempts.")
    break
  else:
    print("Invalid input. Please enter a valid number.")

  if attempts == 5:
    print("You have used all your chances. Game over.")
    exit()
