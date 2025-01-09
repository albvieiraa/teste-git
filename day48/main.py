import os
import time

while True:
    initials = input("Input your initials > ").upper()
    try:
        score = float(input("Input your score (out of about 100.000) > "))
        if score > 100.000:
            print("That's not possible. Try again.")
            continue
    except ValueError:
        print("Invalid score. Please input a valid number.")
        continue

    # Writing to the file
    with open("high.score", "a") as f:  # Usa 'with' para garantir o fechamento do arquivo
        f.write(f"{initials} {score:.3f}\n")  # Salva a pontuação com 3 casas decimais

    print("Added to high score table.")

    # Pergunta se o usuário quer continuar
    choice = input("Do you want to add another score? (yes/no) > ").strip().lower()
    if choice not in ["yes", "y"]:
        print("Exiting. Thank you!")
        break

    # Limpa a tela e reinicia o loop
    time.sleep(1)
    os.system("clear")
