import forca
import adivinhacao


print("*****Bem vindo!*****")
print("**Escolha seu jogo**")
print("********************")
print("(1) Forca  (2) Adivinhação)")

jogo = int(input("O que quer jogar? "))

if jogo == 1:
    print("Jogando Forca")
    forca.jogar()
elif jogo == 2:
    print("Jogando Adivinhação ")
    adivinhacao.jogar()