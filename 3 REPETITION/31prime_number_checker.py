
num = int(input("Digite um número: "))

for i in range(2, num):
    if num % i == 0:
        print(f"{num} não é primo")
        break
    else:
        print(f"{num} é primo")
        break