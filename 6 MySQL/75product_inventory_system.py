from app import conectar
import os

conn = conectar()
cursor = conn.cursor()

inventario = []

def addProd():
    name = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade: "))

    inventario.append(f"{name} - {preco} - {quantidade}")

    cursor.execute("INSERT INTO inventario (nome, preco, quantidade) VALUES (%s, %s, %s)",(name,preco,quantidade))
    conn.commit()


def atuQuant():
    atuProd = input("Prod que sera atualizado: ")
    atuQuant = int(input("Nova quantidade: "))

    cursor.execute("UPDATE inventario SET quantidade = %s WHERE nome = %s",(atuQuant,atuProd))
    conn.commit()


def atuPreco():
    atuProd = input("Prod que sera atualizado: ")
    atuPreco = float(input("Novo preço: "))

    cursor.execute("UPDATE inventario SET preco = %s WHERE nome = %s",(atuPreco,atuProd))
    conn.commit()


def mostrarProds():
    cursor.execute("SELECT nome FROM inventario")
    produtos = cursor.fetchall()
    print("Produtos registrados:")
    for i in produtos:
        print(i[0])

while True:

    op = int(input("\n" \
            "Adicionar prod: 1\n" \
            "Atualizar quant: 2\n" \
            "Atualizar preço: 3\n" \
            "Mostrar produtos: 4\n" \
            "Sair: 5\n"
            "Digite: "))
    
    os.system('cls')

    if op == 1:
        addProd()
    elif op == 2:
        atuQuant()
    elif op == 3:
        atuPreco()
    elif op == 4:
        mostrarProds()
    elif op == 5:
        break
    else:
        print("Opção invalida!") 

cursor.close()
conn.close()
