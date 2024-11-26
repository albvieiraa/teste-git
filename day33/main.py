import os, time

myList = []

def printList():
  print()  
  for item in myList:
    print(item)
  print() 

while True:
  menu = input("\nTo Do List Manager\n\nDo you want to view, add or edit the todo list?\n")
  if menu == "view":
    print(myList)
  elif menu == "add":
    item = input("What do you want to add?\n")
    myList.append(item)
  elif menu == "edit":
    item = input("What do you want to remove?\n")
    if item in myList:
      myList.remove(item)
    else:
      print(f"{item} was not in the list")