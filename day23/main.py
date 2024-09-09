print("Replit Login System")

def Login():
  while True:
    username = input("What is your username? > ")
    password = int(input("What is your password? > "))
    if username == "maryllian" and password == 1234:
      print("Welcome to Replit!")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!")
      continue

Login()
  