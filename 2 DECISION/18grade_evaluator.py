
nota = float(input("Informe sua nota (0-100): "))

if nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
elif nota >= 0:
    print("F")
else:
    print("Nota fora do padrão")
