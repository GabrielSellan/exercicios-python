
num = int(input("Digite um número para saber seus divisores: "))

print("Seus divisores são: ")
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=" ")