
import os
print("Vamos começar seu carrinho de compras! ")

cart = []
while True:
    
    mss = int(input("\nDeseja adicionar um item? Digite: 1\n"
                "Deseja ver o carrinho? Digite: 2\n"
                "Deseja remover um item? Digite: 3\n"
                "Deseja sair? Digite: 4\n")
                )
    os.system('cls')

    if mss == 1:
        item = input("\nInforme o item que deseja adicionar: ")
        cart.append(item)
    elif mss == 2:
        for i in cart:
            print(i)
    elif mss == 3:
        item_rem = input("\nQual item deseja remover?\n"
            "Informe: ")
        if item_rem in cart:
            cart.remove(item_rem)
        else:
            print("\nEste item não está em seu carrinho!")
    elif mss == 4:
        print("\nSeu carrinho ficou assim:")
        for i in cart:
            print(i)
        break
