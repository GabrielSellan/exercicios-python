
num1 = float(input("Informe um número: "))
num2 = float(input("Informe outro número: "))

if num1 > num2:
    print(f"{num1} é maior")
elif num1 < num2:
    print(f"{num2} é maior")
elif num1 == num2:
    print("Os números são iguais")