
print("Lista 1")
lista1 = []
while True:
    numString = input("Digite um número ou 'Pare' para parar: ")

    if numString == "Pare":
        break
    
    num = int(numString)
    lista1.append(num)

print("Lista 2")
lista2 = []
while True:
    numString = input("Digite um número ou 'Pare' para parar: ")

    if numString == "Pare":
        break
    
    num = int(numString)
    lista2.append(num)

comuns = list(set(lista1) & set(lista2))
print(f"{comuns} aparecem am ambas as listas")