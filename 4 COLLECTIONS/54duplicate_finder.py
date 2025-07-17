
lista = []
while True:
    numString = input("Digite um número ou 'Pare' para parar: ")

    if numString == "Pare":
        break
    
    num = int(numString)
    lista.append(num)
    

duplicados = []
vistos = set()

for item in lista:
    if item in vistos and item not in duplicados:
        duplicados.append(item)
    vistos.add(item)

print(duplicados)