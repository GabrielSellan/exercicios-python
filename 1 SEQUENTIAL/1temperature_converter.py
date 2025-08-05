# Converte de Celsius para Fahrenheit e Kelvin

celsius = int(input("Digite a temperatuda em Celsius (°C): "))

fahrenheit = celsius * 1.8 + 320
kelvin = celsius + 273.15

print(f"A temperatura em Fahrenheit é de: {fahrenheit}F, e em Kelvin de: {kelvin}K")