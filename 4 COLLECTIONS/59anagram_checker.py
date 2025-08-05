
palavra1 = input("Digite a primeria palavra: ")
palavra2 = input("Digite a segunda palavra: ")

listaP1 = list(palavra1)
listaP2 = list(palavra2)

if sorted(listaP1) == sorted(listaP2):
    print("Formam um anagrama")
else:
    print("Não formam um anagrama")