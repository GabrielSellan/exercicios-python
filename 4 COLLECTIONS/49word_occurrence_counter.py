import re

setenca = input("Digite um texto: \n")
setenca = re.sub(r'[^\w\s]', '', setenca)
lista = setenca.split(" ")

contagem = {}
for i in lista:
    if i in contagem:
        contagem[i] += 1
    else:
        contagem[i] = 1


for palavra, quant in contagem.items():
    print(f"A palavra '{palavra}' aparece {quant} vez(es) no texto.")