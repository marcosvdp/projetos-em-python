import random

def jogar():

    boas_vindas()

    palavra_secreta =  escolha_da_palavra()

    letras_acertadas = ['_' for letra in palavra_secreta]

    erros = 0
    enforcou = False
    acertou = False

    print("A palavra é " + str(letras_acertadas))
    print("Você tem 6 tentativas, boa sorte!")

    while(not enforcou and not acertou):

        chute = input("Qual Letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Erros: {}".format(erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou, parabéns!")
    else:
        print("Você perdeu! :(")
    print("Fim do jogo ")


def boas_vindas():
    print("**************************")
    print("Seja bem vindo e boa sorte")
    print("**************************")

def escolha_da_palavra():
    arquivo = open("banco de palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


if(__name__ == "__main__"):
    jogar()