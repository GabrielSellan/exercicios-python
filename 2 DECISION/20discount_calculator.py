
preco = float(input("Informe o preço: "))

if preco > 100:
    novo_preco = preco - (preco * 0.1)
    print(f"Sua conta ficou R${novo_preco}")
else:
    print(f"Sua conta ficou R${preco}")