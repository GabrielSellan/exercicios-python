
x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

if x == 0 and y == 0:
    print("O ponto está na origem.")
elif x == 0:
    print("O ponto está no eixo Y.")
elif y == 0:
    print("O ponto está no eixo X.")
elif x > 0 and y > 0:
    print("O ponto está no Quadrante I.")
elif x < 0 and y > 0:
    print("O ponto está no Quadrante II.")
elif x < 0 and y < 0:
    print("O ponto está no Quadrante III.")
else:
    print("O ponto está no Quadrante IV.")
