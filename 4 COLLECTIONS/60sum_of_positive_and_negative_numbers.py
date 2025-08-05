
lista = []
while True:
    numString = input("Digite um número positivo ou negativo, ou 'Pare' para parar: ")

    if numString == "Pare":
        break
    
    num = int(numString)
    lista.append(num)


listaPosi = []
listaNega = []
for i in lista:
    if i > 0:
        listaPosi.append(i)
    else:
        listaNega.append(i)


somaPosi = 0
for i in listaPosi:
    somaPosi += i
print(f"A soma de positivos é: {somaPosi}")

somaNega = 0
for i in listaNega:
    somaNega += i
print(f"A soma de positivos é: {somaNega}")