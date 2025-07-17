


def intersecList(a,b):
    c = list(set(a) & set(b))
    return c

print("Lista 1")
lista1 = []
while True:
    numString = input("Digite um algo ou 'Pare' para parar: ")

    if numString == "Pare":
        break
    
    lista1.append(numString)

print("Lista 2")
lista2 = []
while True:
    numString = input("Digite um algo ou 'Pare' para parar: ")

    if numString == "Pare":
        break
    
    lista2.append(numString)

lista3 = intersecList(lista1, lista2)
print("Elementos que aparecem em ambas as listas: ")
for i in lista3:
    print(i)