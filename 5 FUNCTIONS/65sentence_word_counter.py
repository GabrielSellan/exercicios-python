

def separaFrase(a):
    fraseSep = a.split(" ")
    dicionario = {}
    
    for palavra in fraseSep:
        if palavra in dicionario:
            dicionario[palavra] += 1
        else:
            dicionario[palavra] = 1

    print(dicionario)

frase = input("Digite uma frase: ")
separaFrase(frase)
