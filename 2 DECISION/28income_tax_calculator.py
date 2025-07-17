#Até R$ 1.000: 5% de imposto
#De R$ 1.001 a R$ 5.000: 10% de imposto
#De R$ 5.001 a R$ 10.000: 15% de imposto

valor = float(input("Informe o valor para o calculo do imposto: "))

if valor <= 1000:
    imposto = valor * 0.05
elif valor <= 5000:
    imposto = valor * 0.10
elif valor <= 10000:
    imposto = valor * 0.15
else:
    imposto = valor * 0.20

print(f"Você deve pagar R${imposto:.2f} de imposto.")