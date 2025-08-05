
# Solicita ao usuário um número
n = int(input("Digite um número: "))

# Loop externo para o número de linhas
for i in range(1, n + 1):
    # Imprime espaços para o alinhamento à direita
    print(" " * (n - i), end="")
    # Imprime as estrelas
    print("*" * i)
