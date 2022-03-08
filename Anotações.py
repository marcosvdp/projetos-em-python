print("Hello world")
# assim q se comenta
# drawing shapes:
print("   /|")
print("  / |")
print(" /  |")
print("/___|")
# python executa os comandos em ordem. A ordem importa

# variables and data types

character_name = "Maneco" # string (plain text) e so elas precisam de ""
caracther_age = "37"   # numbers, aceita todos os tipos de numero
is_male = True  # boolean (true or false)

#print("Tinha um homem chamado de " + character_name +", ")
#print("Ele tinha " + caracther_age +" anos. ")
#character_name = "Margorino"
#print("Ele gostava muito do nome " + character_name +". ")
#print("Mas não gostava de ter " + caracther_age +" anos.")

#variaveis vão auxiliar e facilitar a escrita do codigo
#definindo valores que, caso sejam alterados, alteram o mesmo no codigo, sem precisar fazer manualmente
# melhora o controle e o manejo do codigo
# data types: string, numbers, boolean(true or false) são os mais basicos


#working with strings
#print("academia\ngirafa")  #  \n faz o texto se dividir em duas linhas ao ser executado

#print("marcos\"estudando") # o \ é usado para possibilitar a visualização de " dentro da string

phrase = "Academia da Girafa"
#print("eu estudo na " + phrase)  concatenar string

print(phrase.upper()) #upper e lower
#funções para alterar string em letras maisculas e minusculas
print(phrase.islower())  #boolean pra checar a veracidade
print(phrase.upper().isupper()) #podem ser colocadas em sequencia
print(len(phrase)) #numero de characters na string
print(phrase[0]) #para selecionar apenas uma das letras da string
#a contagem de characters começa em zero
print(phrase.index("iraf")) #para identificar a posição da letra na string, ou onde uma sequencia se inicia
# () o valor dado a uma função é chamado de parametro/parameter
print(phrase.replace("Girafa", "Elefante"))  #serve para substituir palavras e letras dentro da string

#BUSCAR OUTRAS FUNÇÕES PARA TESTAR

#WORKING WITH NUMBERS
print(-4.14) #para exibir o numero, seja ele como for
print(2+4.5)  #operações basicas podem ser feitas +-*/
print(3*(2+1)) #os parenteses podem ser usados para definir a ordem das operações
print(10%3) #modulate: dividi o primeiro numero pelo segundo e informa o que sobra da operação
my_num = -5
print(my_num) #numeros podem ser armazenados dentro de variaveis
print(str(my_num) + " é meu numero favorito.") #para converter number em string
#alem de converter em string, adicionar texto a frase, concatenando
print(abs(my_num)) #para receber o valor absoluto do numero
print(pow(3, 2))  #function para fazer potenciação
print(max(4, 6)) #para informar qual valor informado é maior
#o contrario é o "min"
print(round(4.8)) # para arredondar numeros

from math import *
#para importar outras funções matematicas para o python
print(floor(3.5)) # para cortar casa decimal
print(ceil(3.5)) # para arredondar pra cima o valor
print(sqrt(36))  #para calcular a raiz quadrada do numero



#getting input from users
#armazenar informações de usuarios e guardar nas variaveis e usa-la

#name = input("Insira seu nome:")
#python vai permitir nesses casos q usuarios enviem informações para o codigo
# definindo a variavel referente a informação a ser enviada
#age = input("Insira sua idade:")
#possivel coletar multiplas informações para armazenar na variavel
#print("Hello" + name + "! You are " + age)
# o value é coletado e aplicado à variavel ao qual está ligada


#Building a basic calculator

#num1 = input("Insira um numero:")
#num2 = input("Insira outro numero:")

#result = int(num1) + int(num2)

#result = float(num1) + float(num2)

#print(result)
# se atentar pois por default, python vai transformar inputs de users em strings
#mesmo que sejam numeros
# int para deixar de ser lido como string e ser lido como numero inteiro
#com a function "int", numero quebrados não podem ser lidos e um erro aparece

#a function "float" permite que numeros quebrados sejam coletados como informaçõese inseridos na variavel de forma correta

#Lists
#nome precisa ser descritivo do que a lista vai conter

#listas possibilitam armazenar multiplos dados dentro da variavel
#qualquer tipo de informação pode ser armazenado: numbers, strings, boolean

friends = ["Ana", "Maria", "Jose", "Mario", "Margarida"]
print(friends[1])
friends[1] = "Margot"
print(friends[1])
print(friends[-1])
print(friends[2:])
print(friends[1:4])
    # o negativo começa a contagem da posição de tras pra frente
    #assim, a busca inicia-se a partir do objeto referido e pega ele e todos os outros elementos seguintes
    #é possivel tbm pegar apenas alguns dos elemento da lista

# list functions

lucky_numbers = [1,32,6,17,15,5,21]
friends = ["Ana", "Maria","Maria", "Jose", "Mario", "Margarida"]
# friends.extend(lucky_numbers)  # junta diferentes listas
friends.append("Marcos") # adiciona mais algo a lista
friends.insert(1, "Kelly") #para inserir outro valor a lista existente, definindo sua posição nela
#friends.remove("Margarida") #para remover valores especificos da lista
#friends.clear()   caso deseje limpar a lista por completo
friends.pop()  #remove o ultimo elemento na lista
print(friends.index("Ana")) #para verificar se um valor está na lista
print(friends.count("Maria")) #para saber quantos elementos iguais existem na lista
#friends.sort()  #coloca em ordem alfabetica
#lucky_numbers.sort()  #ou em ordem crescente, em caso de numeros
lucky_numbers.reverse() # inverte a ordem original da lista
friends2 = friends.copy() #para criar outra lista igual a uma ja existente
friends.sort()
print(friends2)
print(friends)
print(lucky_numbers)

# Tuples
# para armazenar dados, de forma similar a lista
#mas o dados armazenados não podem ser alterados como na lista
# tuples são mais para situações especiais e especificas
coordinates = (4,10) #tuple
best_coordinates = [(1,4),(5,7),(7,8)] #list of tuples
print(coordinates)
print(coordinates[1]) #os elementos podem ser acessados mas não alterados
print(best_coordinates)

#functions
# def para python saber q queremos usar functions
# Python indentation is a way of telling a Python interpreter that the group of statements belongs to a particular block of code
#functions podem ser varios dados para serem utilizados dentro dela
#string, boolean, arrays são aceitos dentro das functions

#def say_hi(name, age):
    print("Hello " + name + " you are " + age)

#print("top")
#say_hi("Marcos", "26")      # call the function
#say_hi("Marquinho", "27")
#print("botton")

#name = input("Say your name: ")
#age = input("Say your age: ")

#def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

#say_hi(name, age)

#numa função, ao dar enter, um espaço automatico é gerado, e o codigo tem q estár alinhado, para ser entendido como função
# call the function: para especificar que queremos que a função seja executada
# parameters: informações para adicionar a função

#return statement
#return serve para situações onde vc quer um retorno de informações da função
#demonstra os valores obtidos dentro da função
#def cube(number):
    return number*number*number

#result = cube(4)
#print(result)
#não é possivel adicionar nada na função apos o return

# if statement e comparisons

is_male = False
is_tall = False

if is_male and is_tall:
    print("Você é um homem alto")
elif is_male and not(is_tall):
    print("Você é um homem baixo")
elif not(is_male) and is_tall:
    print("Você é uma mulher alta")
else:
    print("Você é uma mulher baixa")

#if para a condição a ser checada
#else como a alternativa a ser seguida se a condição inicial for falsa
#elif para checar mais de uma condição na mesma sentença
#and e or para definir a situação
def max_number(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_number(75, 485, 75))
#é possivel usar para fazer comparações, desde que no fim, a sentença seja possivel de ser interpretada como boolean
# é possivel comparar strings tbm, no lugar de numbers
# substituindo o >= (sinal de comparação) por == para checar se são iguais ou != se quer saber se não são iguais

# Dictionaries
# É um tipo de dado que possibilita armazenar KEY VALUE PAIRS
#Voce armazena dados e informações e consegue acessar apartir dos KEY vALUE PAIRS
# Exemplo de dictionarie. Usar sempre {}

monthConversions = {
    "Jan": "Janeiro",
    "Fev": "Fevereiro",
    "Mar": "Março",
    "Abr": "Abril",
    "Mai": "Maio",
    "Jun": "Junho",
    "Jul": "Julho",
    "Ago": "Agosto",
    "Set": "Setembro",
    "Out": "Outubro",
    "Nov": "Novembro",
    "Dez": "Dezembro",
}
# O primeiro valor é a KEY e o segundo é o VALUE
# Todas as KEY precisam ser unicas

print(monthConversions["Jul"])
# Se referir diretamente ao nome dado ao dicionario e usar [] para o elemento
print(monthConversions.get("Jun"))
print(monthConversions.get("Jin", "Invalid Key"))
# O caso acima é para situações onde o valor inserido n está listado
# Sendo possivel adicionar um retorno para o caso do valor n ser encontrado
# Numeros podem ser KEYS tbm, desde que sejam valores unicos

# While Loop
# É uma função que permiter criar um loop e executar o codigo repetidamente
# Até que uma condições requerida seja atingida

i = 1
# O que vem apos declarar um loop, é a condição dele, o LOOP GUARD
while i <= 10:
    print(i)
    i = i + 1  # i += 1 é outra forma de fazer essas somas
print("Fim do loop ")

FORMATAÇÃO
print('Formatação de Floats')
print("R$ {:.2f}".format(1.59))

print("R$ {:7.2f}".format(1234.50))

print("Formatação de inteiros")
print("R$ {:07d}".format(4))
print("Data {:02d}/{:02d}".format(13, 6))

#f-strings ou formatted string literals
nome = "Marcos"
print(f"Meu nome é {nome}")
print(f"Meu nome é {nome.upper()}")

#random
#randrange  delimita o valor maximo para o numero gerado, do valor inicial(ou 0 caso n seja informado) até o limite -1
