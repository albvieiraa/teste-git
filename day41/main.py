# Creating function to dictionary

def creatWebsite():
  websiteInfo = {} # Empty dictionary

  websiteInfo["name"] = input("Enter website name: ")
  websiteInfo["URL"] = input("Enter website URL: ")
  websiteInfo["description"] = input("Enter website description: ")
  websiteInfo["rating"] = input("Input the rating (0-5):")

  return websiteInfo

# Print the dictionary
website = creatWebsite()

print("\n🌟Website Rating🌟")
for key, value in website.items():
  print(f"{key.capitalize()}:{value}")