print("Calculating the seconds of this Year")
print("------------------------")

days_this_year = int(input("How many days are in this year? "))

hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60

result = days_this_year * hours_in_day * minutes_in_hour * seconds_in_minute

leapyear_result = (days_this_year * hours_in_day * minutes_in_hour * seconds_in_minute) + 1

if days_this_year == 366:
  print(f"Number of seconds in a leap year are {leapyear_result}")
elif days_this_year == 365:
  print(f"Number of seconds in a year are {result}")
else:
  print("Invalid input")
