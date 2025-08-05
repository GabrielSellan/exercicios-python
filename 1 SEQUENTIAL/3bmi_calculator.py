# Calculo de BMI

print("Para calcular seu IMC forneça as seguintes informações: ")

peso = float(input("Seu peso em Kg: "))
altura = float(input("Sua altura em metros: "))
idade = float(input("Sua idade: "))

IMC = peso / (altura * altura)
print(f"Seu IMC é {IMC}")

if IMC < 18.5:	
    print("Magreza")
elif IMC < 24.9: 
    print("Normal")
elif IMC < 29.9:
    print("Sobrepeso")
elif IMC < 34.9:
    print("Obesidade grau I")
elif IMC < 39.9:
    print("Obesidade grau II")
else:
    print("Obesidade grau III")    
	