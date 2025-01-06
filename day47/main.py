import random

# Dicionário com as cartas
cards = {
    "Professor X": {
        "Inteligência": 90,
        "Beleza": 50,
        "Habilidade em Programação": 85,
        "Grau de Careca": 100,
    },
    "Professor Y": {
        "Inteligência": 75,
        "Beleza": 70,
        "Habilidade em Programação": 95,
        "Grau de Careca": 40,
    },
}

# Pontuação dos jogadores
player1_score = 0
player2_score = 0

print("Bem-vindo ao jogo Super Trunfo! 🚀")
print("Escolha uma carta e compare atributos para ganhar pontos.\n")

# Loop principal do jogo
while True:
    print("\nCartas disponíveis: ", ", ".join(cards.keys()))
    print("Jogador 1, escolha sua carta:")
    player1_card = input("Digite o nome da carta: ").strip()
    
    if player1_card not in cards:
        print("Carta inválida. Tente novamente.")
        continue

    print("\nJogador 2, escolha sua carta:")
    player2_card = input("Digite o nome da carta: ").strip()
    
    if player2_card not in cards:
        print("Carta inválida. Tente novamente.")
        continue

    print("\nAtributos disponíveis: ", ", ".join(cards[player1_card].keys()))
    print("Jogador 1, escolha um atributo para comparar:")
    chosen_attribute = input("Digite o atributo: ").strip()

    if chosen_attribute not in cards[player1_card]:
        print("Atributo inválido. Tente novamente.")
        continue

    # Mostra os valores dos atributos escolhidos para cada carta
    player1_value = cards[player1_card][chosen_attribute]
    player2_value = cards[player2_card][chosen_attribute]

    print(f"\n{player1_card} tem {chosen_attribute}: {player1_value}")
    print(f"{player2_card} tem {chosen_attribute}: {player2_value}")

    # Determina quem ganha o turno
    if player1_value > player2_value:
        print(f"Jogador 1 vence este turno! 🏆")
        player1_score += 1
    elif player1_value < player2_value:
        print(f"Jogador 2 vence este turno! 🏆")
        player2_score += 1
    else:
        print("Empate neste turno! 😲")

    # Exibe a pontuação atual
    print(f"\nPlacar: Jogador 1: {player1_score} | Jogador 2: {player2_score}")

    # Pergunta se os jogadores querem continuar
    play_again = input("\nQuer jogar outro turno? (s/n): ").strip().lower()
    if play_again != 's':
        print("Fim de jogo! 🎉")
        print(f"Placar final: Jogador 1: {player1_score} | Jogador 2: {player2_score}")
        break
