import os


lista = []

def fatoriando(a):
    fatoriais = ['Num - Fatorial']
    somaFat = 1
    for num in a:
        for i in range(1, num+1):
            somaFat *= i
        fatoriais.append(f"{num} - {somaFat}")
        somaFat = 1
    
    for y in fatoriais:
        print(y)



while True:
    numString = input("Digite um número ou 'Pare' para parar: ")

    if numString == "Pare":
        break
    
    num = int(numString)
    lista.append(num)

os.system('cls')

fatoriando(lista)