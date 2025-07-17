

lista = []


def dick(l):
    dick = {}
    for i in l:
        if i in dick:
            dick[i] += 1
        else:
            dick[i] = 1

    print(dick)

while True:
    numString = input("Digite um algo ou 'Pare' para parar: ")

    if numString == "Pare":
        break

    lista.append(numString)


dick(lista)