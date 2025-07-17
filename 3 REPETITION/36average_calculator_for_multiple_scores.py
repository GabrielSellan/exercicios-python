
pontos = " "
soma = 0
i = 0

while pontos != 'pronto':
    pontos = input("Digite uma pontuação ou 'pronto' para calcular a média: ")

    if pontos == 'pronto':
        print(f"Sua média foi de {soma/i}")
        break

    soma += float(pontos)
    i += 1