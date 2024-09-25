print("30 Days Down - What did you think about each day?")
def main():
  for i in range (1,31):
    thought = input(f"Day {i}: \n")
    output = f"You thought Day {i} was {thought}"
    print(output)

main()