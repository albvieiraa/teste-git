print(f"{'=' * 5} Fill in the blank lyrics! {'=' * 5}")

count = 0

while True:
  print("Never going to ______ you up.")
  word = input("What is the missing word? ")
  if word != "give":
    count =+ 1
    print("Nope, try again.")
  else:
    print(f"Well done! It only took you {count} attempts.")
    break