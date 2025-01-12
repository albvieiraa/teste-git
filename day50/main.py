import os
import time
import random

# Função principal
def idea_storage():
    while True:
        # Menu principal
        print("=== Idea Storage System ===")
        print("1. Add an idea")
        print("2. Load a random idea")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            # Adicionar uma ideia
            add_idea()
        elif choice == "2":
            # Carregar uma ideia aleatória
            load_random_idea()
        elif choice == "3":
            # Sair do programa
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Pausa e limpeza de tela
        time.sleep(1)
        os.system("clear" if os.name == "posix" else "cls")


# Função para adicionar uma ideia
def add_idea():
    idea = input("Enter your idea: ").strip()
    if idea:
        with open("my.ideas", "a") as file:
            file.write(idea + "\n")
        print("Idea added successfully!")
    else:
        print("No idea entered. Returning to menu.")


# Função para carregar uma ideia aleatória
def load_random_idea():
    try:
        with open("my.ideas", "r") as file:
            ideas = file.readlines()
        if ideas:
            random_idea = random.choice(ideas).strip()
            print(f"Here's a random idea: {random_idea}")
            time.sleep(3)  # Mostra a ideia por alguns segundos
        else:
            print("No ideas found in the file.")
    except FileNotFoundError:
        print("The file 'my.ideas' does not exist. Add some ideas first.")


# Executa o programa
if __name__ == "__main__":
    idea_storage()
