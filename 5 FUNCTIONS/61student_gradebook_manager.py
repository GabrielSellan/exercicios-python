import os

notas = []

def addNota(a):
    notas.append(a)


def delNota(a):
    if a in notas:
        notas.remove(a)


def verNotas():
    for i in notas:
        print(i)


def medNotas():
    media = 0
    acimaMed = []
    
    for i in notas:
        media += i
    media = media/len(notas)

    for i in notas:
        if i > media:
            acimaMed.append(i)
    
    print(acimaMed)

while True:
    campo = input("O que precisa?\n"
                    "Adicionar nota:            1\n"
                    "Remover nota:              2\n"
                    "Ver notas:                 3\n"
                    "Ver notas acima da média:  4\n"
                    "Parar programa:            5\n")
    
    os.system('cls')
    
    if campo == '1':
        nota = float(input("Informe a nota: "))
        addNota(nota)
    elif campo == '2':
        nota = float(input("Informe a nota: "))
        delNota(nota)
    elif campo == '3':
        verNotas()
    elif campo == '4':
        medNotas()
    elif campo == '5':
        break
    else:
        print("Digito inválido")
    
    