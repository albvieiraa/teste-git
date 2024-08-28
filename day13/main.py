print("Exam Grader Calculator \n")
examName = input("Name of exam: ")
maxScore = int(input("Max. Possible Score: "))
yourScore = int(input("Your score: "))
percentage = round(yourScore / maxScore * 100)

if yourScore < 0:
  print("Please enter a valid score")
else:
  if percentage >= 80:
    print(f"You got {percentage}% which is an A. Congratulations!")
  elif percentage >= 70:
    print(f"You got {percentage}% which is an B. Well done!")
  elif percentage >= 60:
    print(f"You got {percentage}% which is an C. Not bad!")
  elif percentage >= 50:
    print(f"You got {percentage}% which is an D. You can do better!")
  elif percentage < 50:
    print(f"You got {percentage}% which is an E. You need to study more!")
  else:
    print("Oh no, it's somenting wrong! Try again!")