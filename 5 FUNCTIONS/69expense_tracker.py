import os

despesas = []

def addDesp():
    valor = input("Valor da despesa: ")
    descricao = input("Descreva a despesa: ")
    despesas.append(f"{descricao} - {valor}")

def delDesp():
    despDel = input("Informe a descrição da despesa a ser deletada: ")
    for i in despesas:
        descDesp = i.split(" - ")
        if descDesp[0] == despDel:
            despesas.remove(i)

def viewDesp():
    for i in despesas:
        print(i)

def totDesp():
    soma = 0
    for i in despesas:
        valDesp = i.split(" - ")
        soma += float(valDesp[1])
    print(f"O total das despesas deram: R${soma}")


while True:
    seletor = input("Adicionar despesas: 1\n" \
                    "Remover despesa: 2\n" \
                    "Ver despesas: 3\n" \
                    "Valor total das despesas: 4\n" \
                    "Parar programa: 5\nDigite: ")
    os.system('cls')
    
    if seletor == '1':
        addDesp()
    elif seletor == '2':
        delDesp()
    elif seletor == '3':
        viewDesp()
    elif seletor == '4':
        totDesp()
    elif seletor == '5':
        break
    else:
        print("Valor inválido")