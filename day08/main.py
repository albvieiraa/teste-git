name = input("Who are you? ")
print(f"Hello {name}")
joke = "This answer is so wrong that it looks like a Monday plan: full of good intentions, but nothing works!"
dow = input("What day the day of the week? ").lower()
if dow == "monday":
  print("New week, new opportunities!")
elif dow == "tuesday":
  print("Stay focused and keep moving forward.")
elif dow == "wednesday":
  print("Don't give up now, the best is yet to come.")
elif dow == "thursday":
  print("Celebrate your small victories.")
elif dow == "friday":
  print("You deserve a break.")
elif dow == "saturday":
  print("Relax and enjoy your weekend.")
elif dow == "sunday":
  print("Recharge your batteries for a new week.")
else:
  print(joke)