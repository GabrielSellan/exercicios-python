
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))
nota4 = float(input("Digite a nota da quarta prova: "))
nota5 = float(input("Digite a nota da quinta prova: "))

media = (nota1+nota2+nota3+nota4+nota5) / 5

if media > 6:
    print("Passou")
else:
    print("Falhou")
