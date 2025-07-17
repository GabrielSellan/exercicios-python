
lista = []
while True:
    numString = input("Digite uma pontuação ou 'Pare' para parar: ")

    if numString == "Pare":
        break
    
    num = float(numString)
    lista.append(num)

ordDec = sorted(lista, reverse=True)
for i in range(0,3):
    print(ordCresc[i])