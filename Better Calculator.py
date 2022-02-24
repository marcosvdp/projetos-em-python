num1 = float(input("Insira um numero: "))
operator = input("Insira a operação: ")
num2 = float(input("Insira numero: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Operação invalida")
