
lista = []
while True:
    num_s = input("Informe os números ou 'n' para parar: ")
    if num_s == 'n':
        break
    lista.append(float(num_s))

lista_reversa = []
for i in reversed(lista):
    lista_reversa.append(i)


print(f"Lista original: {lista}")
print(f"Lista reversa: {lista_reversa}")