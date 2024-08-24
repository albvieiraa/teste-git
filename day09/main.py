print("👴 Generation Identifier 👦")
year = int(input("📅 Which year were you born? "))
if year <= 1925:
  print(f"You born in {year}, so you are a Traditionalist")
elif year >= 1947 and year < 1965:
  print(f"You born in {year}, so you are a Baby Boomer")
elif year >=1965 and year < 1982:
  print(f"You born in {year}, so you are a Generation X")
elif year >= 1982 and year < 1996:
  print(f"You born in {year}, so you are a Millenial")
elif year >=1996:
  print(f"You born in {year}, so you are a Generation Z")
else:
  print("You are not born yet")