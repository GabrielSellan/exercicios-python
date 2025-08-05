lista = []
while True:
    numString = input("Digite um número ou 'Pare' para parar: ")

    if numString == "Pare":
        break
    
    num = int(numString)
    lista.append(num)

listEven = []
listOdd = []

for i in lista:
    if i % 2 == 0:
        listEven.append(i)
    else:
        listOdd.append(i)

print(f"Pares: {listEven}")
print(f"Impares: {listOdd}")