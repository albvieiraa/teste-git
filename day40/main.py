def contact_list():
  print("🌟Contact Card🌟\n")
  name = input("Input your full name > ").title()
  birth = input("Input your date of birth (MM/DD/YYYY) > ")
  phone = input("Input your phone number (ddd)0000-000 > ")
  email = input("Input your email address > ")
  adress = input("Input your adress > ")

  infos = {"name": name, "birth": birth, "phone":      phone, "email": email, "adress": adress}

  message = f"Hi {infos['name']}. Our dictionary says that you were born on {infos['birth']}, we call you on {infos['phone']}, email {infos['email']}, or write to {infos['adress']}."

  print(message)

contact_list()