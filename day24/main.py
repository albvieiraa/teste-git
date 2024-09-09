import random

print("Infinity Dice 🎲")

def roll_dice(sides):
    print("You rolled ", random.randint(1, sides))

while True:
    sides = int(input("How many sides?: "))
    roll_dice(sides)
    play_again = input("Roll again? (yes/no): ")
    if play_again.lower() != "yes":
        break