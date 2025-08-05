# Calculadora de Juros Simples
# I= P * r * t
# I é o juros simples
# P é o principal (valor inicial)
# r é a taxa de juros (em decimal)
# t é o tempo (geralmente em anos)

print("Para calcular o juros simples preciso de algumas informações:")

p = float(input("O valor inicial: "))
r = float(input("A taxa de juros em %: ")) / 100
t = float(input("O tempo em anos: "))

i = p * r * t
print(f"O juros simples vai ser de: R${i:.2f}")