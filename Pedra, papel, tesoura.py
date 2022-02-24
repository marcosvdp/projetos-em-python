import random

user_wins = 0
computer_wins = 0

opções = ["pedra", "papel", "tesoura"]

while True:
    user_input = input("Escolha Pedra/Papel/ Tesoura ou Q para sair: ").lower()
    if user_input == "q":
        break
    if user_input not in opções:
        continue


    random_number = random.randint(0, 2)
    # pedra: 0 papel: 1 tesoura: 2
    computer_pick = opções[random_number]
    print("O computador escolheu", computer_pick + ".")

    if user_input == "pedra" and computer_pick == "tesoura":
        print("Você venceu!")
        user_wins += 1

    elif user_input == "papel" and computer_pick == "pedra":
        print("Você venceu!")
        user_wins += 1

    elif user_input == "tesoura" and computer_pick == "papel":
        print("Você venceu!")
        user_wins += 1

    else:
        print("Você perdeu!")
        computer_wins += 1

print("Voce ganhou", user_wins, "vezes.")
print("O computador ganhou", computer_wins, "vezes")
print("Tchau Tchau!!")
