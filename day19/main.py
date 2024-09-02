print("Loan Calculator\n")

loan = 1000
apr = 0.05
interest = loan * apr

for year in range(10):
  loan += interest
  print(f"Year {year + 1} is {round(loan,2)}")