

lista = []


def delDuplicates(l):
    listaU = []
    count = {}

    for i in l:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for j in count:
        if count[j] == 1:
            listaU.append(j)
    
    print(f"Valores únicos digitados: {listaU}")


while True:
    numString = input("Digite um algo ou 'Pare' para parar: ")

    if numString == "Pare":
        break
    
    lista.append(numString)

delDuplicates(lista)
