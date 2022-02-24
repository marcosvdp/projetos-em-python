# Jogo de adivinhação

palavraSecreta = "tomate"
tentativa = ""
numeroDeTentativas = 0
maximoDeTentativas = 3
semTentativas = False

while tentativa !=  palavraSecreta and not(semTentativas):
    if numeroDeTentativas < maximoDeTentativas:
        tentativa = input("Qual a palavra secreta? ")
        numeroDeTentativas += 1
    else:
        semTentativas = True

if semTentativas:
    print("Suas tentativas acabaram. voce perdeu")
else:
    print("Parabens! Voce ganhou!")
# é possivel usar if no while loop nesse caso para o jogo dar dicas entre uma repetição e outra?


