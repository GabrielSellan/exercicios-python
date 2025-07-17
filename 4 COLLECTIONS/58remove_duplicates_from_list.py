
lista = []
while True:
    numString = input("Digite um número ou 'Pare' para parar: ")

    if numString == "Pare":
        break
    
    num = int(numString)
    lista.append(num)

listaUnico = []
for i in lista:
    if i not in listaUnico:
        listaUnico.append(i)

print(f"Lista sem repetidos: {listaUnico}")