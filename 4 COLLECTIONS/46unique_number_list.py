
lista_num = []

while True:
    nums = input("Digite o númeroque quer adicionar a lista ou 'stop' para parar: ")
    if nums == "stop":
        break

    num = float(nums)
    if num not in lista_num:
        lista_num.append(num)

print("Sua lista: ")
for i in lista_num:   
    print(i, end=" ")
