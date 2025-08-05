# Calculadora simples

n1 = float(input("Informe o primeiro numero: "))
op = input("Qual operação deseja realizar? (+, -, *, /) ")
n2 = float(input("Informe o segundo numero: "))

if op == "+":
    print(n1 + n2)
elif op == "-":
    print(n1 - n2)
elif op == "*":
    print(n1 * n2)
elif op == "/":
    print(n1 / n2)
else:
    print("Operador incorreto")
