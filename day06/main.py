username = input("Insert your username: ")
password = input("Insert your password: ")

if username == "admin" and password =="1234":
  print("Welocome to the program")
elif username == "salesperson" and password == "5678":
  print("Let's start salses")
elif username == "manager" and password == "9101":
  print("Let's start the manager")
else:
  print("You don't have access")