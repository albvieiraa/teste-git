print("🌟 Star Wars Name Generator 🌟")

# Entering with first and last name
firstName = input("Input your first name > ").strip().capitalize()
lastName = input("Input your last name > ").strip().capitalize()

# Slicing first name and last name
firstSlice = firstName[:4]
lastSlice = lastName[:4]

# Combining first and last name, that represent the first name of the Star Wars character
newName = (f"{firstSlice}{lastSlice}").capitalize()

# Entering with mother's maiden name and city of birth
maidenName = input("Input your mother's maiden name > ").strip().capitalize()
city = input("Input the city where you were born > ").strip().capitalize()

# Slicing maiden name and city
maidenSlice = maidenName[:3]
citySlice = city[-3:]

# Combining maiden and city, that represent the last name of the Star Wars character
newLastName = (f"{maidenSlice}{citySlice}").capitalize()

# Printing the Star Wars name
print(f"Your Star Wars name is {newName} {newLastName}")