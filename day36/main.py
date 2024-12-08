nameList = []

# Função para imprimir nomes da lista
def printList():
  print()
  for fullName in nameList:
    print(fullName)
  print()

# Loop para receber nomes
while True:
  firstName = input("What is your first name? ").strip().capitalize()
  lastName = input("What is your last name? ").strip().capitalize()
  fullName = f"{firstName} {lastName}"
  if fullName not in nameList:
    nameList.append(fullName)
  else:
    print("ERROR: Duplicate name")
  printList()