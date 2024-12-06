import os, time

myList = []

def printList():
  print()  
  for item in myList:
    print(item)
  print() 

while True:
  menu = input("\nTo Do List Manager\n\nDo you want to view, add, edit, or remove or delete the to do list?\n")
  if menu == "view":
    print(myList)
  elif menu == "add":
    item = input("What do you want to add?\n").title()
    myList.append(item)
  elif menu == "edit":
    item = input("What do you want to edit?\n").title()
    new = input("What do you want to change it to?\n").title()
    for i in range(0,len(myList)):
      if myList[i]==item:
        myList[i]=new    
  elif menu == "remove":
    item = input("What do you want to remove?\n").title()
    check = input("Are you sure you want to remove this? Yes or Not?\n")
    if check[0] == "Yes":
      if item in myList:
        myList.remove(item)
      else:
        print(f"{item} was not in the list")
  elif menu=="delete":
    check_2 = input("Are you sure you want to delete the list? Yes or Not?\n")
    if check_2=="Yes":
      myList = []
    else:
      print("Okay, we will not delete the list.")
  time.sleep(1)
  os.system('clear')