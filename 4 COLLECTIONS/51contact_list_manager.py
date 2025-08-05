import os
print("Vamos começar a lista de contatos!")

listaCont = []
while True:

    mss = int(input("Se deseja adicionar um contato digite: 1\n"
                "Se deseja ver seus conatos digite: 2\n"
                "Se deseja deletar um contato digite: 3\n")
    )
    os.system('cls')

    if mss == 1:
        nome = input("Informe o nome do contato: ")
        num = input("Informe o numero do contato: ")
        contato = f"{nome} - {num}"
        listaCont.append(contato)
    elif mss == 2:
        for i in listaCont:
            print(i)
    elif mss == 3:
        numDel = input("Informe o numero do contato que deseja deletar: ")
        for contato in listaCont:
            if numDel in contato:
                listaCont.remove(contato)

    