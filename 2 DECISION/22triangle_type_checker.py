
#Triângulo Equilátero: Todos os três lados têm o mesmo comprimento.

#Triângulo Isósceles: Dois lados têm o mesmo comprimento e o outro lado é diferente.

#Triângulo Escaleno: Todos os três lados têm comprimentos diferentes.

print("Informe os 3 lados do triângulo: ")
l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

if l1 == l2 and l1 == l3:
    print("Triângulo Equilátero")
elif l1 == l2 and l1 != l3 or l1 == l3 and l1 != l2 or l2 == l3 and l2 != l1:
    print("Triângulo Isósceles")
elif l1 != l2 and l1 != l3 and l2 != l3:
    print("Triângulo Escaleno")
