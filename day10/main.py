total_bill = float(input("What was the total bill? $ "))
tip_percentage = int(input("What percentage tip would you like to give? 15, 18 or 20? "))
numberOfPeoples = int(input("How many people to split the bill? "))

bill_tip = (tip_percentage / 100) * total_bill + total_bill
bill_person = bill_tip / numberOfPeoples

final_amount = round(bill_person, 2)

print(f"Each person should pay: $ {final_amount}")