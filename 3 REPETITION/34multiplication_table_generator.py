
#Multiplication Table Generator
num = int(input("Digite um numero para ver a tabuada: "))

for i in range(1, 11):
    op = num * i
    print(f"{i} x {num} = {op}")