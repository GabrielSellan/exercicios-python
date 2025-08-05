# Conversor de tempo em minustos para horas e minutos

min = float(input("Informa o tempo em minutos: "))

horas = int(min / 60)
n_min = int(min % 60)

print(f"O tempo foi de {horas} horas e {n_min} minutos")