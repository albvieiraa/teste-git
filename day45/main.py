import os, time

toDoList = []

def menu():
  print("🌟Life Organizer🌟\n")
  answer = input("Welcome to the life organizer. Do you want to: \n * Add \n * View \n * Edit \n * Remove \n")
  print()
  if answer == "add":
    add()
  elif answer == "view":
    view()
  elif answer == "edit":
    edit()
  elif answer == "remove":
    remove()
  else:
    print("Invalid input. Please try again.")

# Create function to each option
def add():
  time.sleep(1)
  os.system("clear")
  task = input("What is the task? > ")
  dueDate = input("When is it due by? > ")
  priority = input("What is the priority? > ")
  row = [task, dueDate, priority]
  toDoList.append(row)
  print("Thanks, this task has been added.")

def view():
  time.sleep(1)
  os.system("clear")
  options = input("Do you want to view all or view priority? \n")
  if options == "all":         
    for row in toDoList:
      for item in row:
        print(item, end=" | ")
      print()
  else: 
    priority = input("What priority? > ")
    for row in toDoList:
      if priority in row:
        for item in row:
          print(item, end=" | ")
        print()
    time.sleep(1)

def edit():
  time.sleep(1)
  os.system("clear")
  edition = input("What do you want to edit? > ")
  for row in toDoList:
    if edition in row:
      toDoList.remove(row)
      task = input("What is the NEW task? > ")
      dueDate = input("When is it due by? > ")
      priority = input("What is the NEW priority?")
      row = [task, dueDate, priority]
      toDoList.append(row)
      print("Thanks, this new task has been added.")
      
def remove():
  time.sleep(1)
  os.system("clear")
  removing = input("What task do you want to remove? > ")
  for row in toDoList:
    if removing in row:
      toDoList.remove(row)

while True:
  menu()
  time.sleep(1)
  os.system("clear")