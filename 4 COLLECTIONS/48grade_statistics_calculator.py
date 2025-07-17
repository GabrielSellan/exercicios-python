import os

notas = []

while True:
    nota_s = input("Informe uma nota ou digite 'n' para parar: ")
    if nota_s == 'n':
        break

    nota = float(nota_s)
    notas.append(nota)

os.system('cls')

soma = 0
for i in notas:
    soma += i
print(f"Sua média foi: {soma/len(notas)}")

print(f"Sua maior nota foi: {max(notas)}")
print(f"Sua menor nota foi: {min(notas)}")