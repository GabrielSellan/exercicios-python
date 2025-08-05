import random

num = random.randint(1, 10)
print("Você tem 6 chances para acertar um número entre 1 e 10\n")

for i in range(7):
    chute = int(input("Digite seu chute: "))

    if chute == num:
        print("Acertou!!!")
        break
    else:
        print("Tente novamente!\n")