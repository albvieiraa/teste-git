print("Multiplication Table - Math Game")

number = int(input("Name your multiples: "))
score = 0

for i in range(1, 11):
  correct_answer = i * number
  print(f"{i} x {number} = ")
  answer = int(input("> "))
  if answer == correct_answer:
    print("You're right!")
    score += 1
  else:
    print(f"That's not correct. It should have been {correct_answer}")

if score == 10:
  print("Wow! A perfect score! 🥳")
else:
  print(f"You got {score} out of 10 correct.")