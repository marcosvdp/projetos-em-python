import random
print("Adivinhe o numero")
total_de_tentativas = 0
numero_random = random.randrange(1,101)
pontos = 1000
print("Escolha a dificuldade do jogo")
print("(1) Fácil (2) Médio (3) Dificil")
nivel = int(input("Defina um nivel: "))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5
# esse mais é por que no range o numero limite não entra na contagem, no caso, o 3 do numero de tentativas não entra, então, adicionando mais um, temos o ajuste
#range(start, stop, [step])
for rodada in range(1, total_de_tentativas + 1):   #for e a função range para não precisar delimitar um valor pra rodada e sim colocar um limite pro loop
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))  #interpolação de strings
    chute_str = input("Digite o seu número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_random == chute
    maior = chute > numero_random
    menor = chute < numero_random

    if chute < 1 or chute > 100:
        print("Escolha um número entra 1 e 100")
        continue

    elif (acertou):
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
            if (rodada == total_de_tentativas):
                print("O numero secreto era {}. Você fez {}".format(numero_random, pontos))
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")
            if (rodada == total_de_tentativas):
                print("O numero secreto era {}. Você fez {}".format(numero_random, pontos))
        pontos_perdidos = abs(numero_random - chute)  #abs para ter apenas numero absolutos
        pontos = pontos - pontos_perdidos



print("Fim do jogo")