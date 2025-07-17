#Primeiros 100 kWh: R$ 0,50 por kWh
#Próximos 200 kWh (101 a 300 kWh): R$ 0,75 por kWh
#Acima de 300 kWh: R$ 1,00 por kWh

consumo = float(input("Informe seu consumo de energia: "))

if consumo <= 100:
    gasto = consumo * 0.5
    
elif consumo <= 300:
    gasto = consumo * 0.75
else:
    gasto = consumo * 1
    
print(f"Sua conta será de R${gasto:.2f}")