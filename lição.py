print("Adivinhe o numero")
numero_secreto = 45
total_de_tentativas = 3
# esse mais é por que no range o numero limite não entra na contagem, no caso, o 3 do numero de tentativas não entra, então, adicionando mais um, temos o ajuste
#range(start, stop, [step])
for rodada in range(1, total_de_tentativas + 1):   #for e a função range para não precisar delimitar um valor pra rodada e sim colocar um limite pro loop
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))  #interpolação de strings
    chute_str = input("Digite o seu número entre 1 e 100: ")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if chute < 1 or chute > 100:
        print("Escolha um número entra 1 e 100")
        continue

    elif (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")



print("Fim do jogo")