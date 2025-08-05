
texto = input("Digite algo: ")
texto_invertido = texto[::-1]

if texto == texto_invertido:
    print("É um palindromo")
else:
    print("Não é um palindromo")