import math

saque = float(input("Qual valor deseja sacar: "))

while True:
    notas = saque / 100
    if notas >= 1:
        print(f"{math.floor(notas)} notas de R$100")
        saque -= 100 * math.floor(notas)
    
    notas = saque / 50
    if notas >= 1:
        print(f"{math.floor(notas)} notas de R$50")
        saque -= 50 * math.floor(notas)

    notas = saque / 20
    if notas >= 1:
        print(f"{math.floor(notas)} notas de R$20")
        saque -= 20 * math.floor(notas)

    notas = saque / 10
    if notas >= 1:
        print(f"{math.floor(notas)} notas de R$10")
        saque -= 10 * math.floor(notas)

    notas = saque / 5
    if notas >= 1:
        print(f"{math.floor(notas)} notas de R$5")
        saque -= 5 * math.floor(notas)

    notas = saque / 2
    if notas >= 1:
        print(f"{math.floor(notas)} notas de R$2")
        saque -= 2 * math.floor(notas)
    
    notas = saque / 1
    if notas >= 1:
        print(f"{math.floor(notas)} notas de R$1")
        saque -= 1 * math.floor(notas)

    break


