import os, time, random


print("⚔ Character Builer\n")

def Dice(side):
  result = random.randint(1,side)
  return result

def Health():
  health_stat = ((Dice(6)*Dice(12))/2) + 10
  return health_stat

def Strength():
  strength_stat = ((Dice(6)*Dice(8))/2) + 12
  return strength_stat

while True:
  name = input("What is your character's name? ")
  type = input("What is your character's type? (Human, Elf, Wizard, Orc): ")

  print(name)
  print(f"HEALTH: {Health()} \nSTRENGTH: {Strength()}")
  print("May your name go down in Legend... \n")

  again = input("Again? \n").lower()
  if again == "no":
    break
  time.sleep(2)
  os.system("clear")
  


