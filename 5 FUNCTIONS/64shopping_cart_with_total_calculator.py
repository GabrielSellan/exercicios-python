
import os

print("Vamos começar seu carrinho de compras! ")

cart = []

def addItem():
        item = input("\nInforme o item que deseja adicionar: ")
        preco = float(input("Informe o preço do item: "))
        prod = f"{item} - {preco}"
        cart.append(prod)
        
def delItem():
        item = input("\nQual item deseja remover?\n"
            "Informe: ")
        for prodPrice in cart:
            if item in prodPrice:
                cart.remove(prodPrice)
            else:
                print("\nEste item não está em seu carrinho!")         
            
def cost():
    total = 0
    for i in cart:
        preco = float(i.split(" - ")[1])
        total += preco
    print(f"O valor total dos itens deu: {total}")


while True:    
    mss = int(input("\nDeseja adicionar um item? Digite: 1\n"
                "Deseja remover um item? Digite: 2\n"
                "Deseja ver o valor total do carrinho: 3\n"
                "Deseja sair? Digite: 4\n")
                )
    os.system('cls')

    if mss == 1:
        addItem()
    elif mss == 2:
        delItem()
    elif mss == 3:
        cost()
    elif mss == 4:
        break
