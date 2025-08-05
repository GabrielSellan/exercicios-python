# Quadratic Equation Solver
import math

print("Vamos resolver a raiz quadrada!")

a = float(input("Informe o valor de (a) "))
b = float(input("Informe o valor de (b) "))
c = float(input("Informe o valor de (c) "))

delta = (b*b) - (4 * a * c)

x1 = (-b + math.sqrt(delta)) / (2 * a)
x2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"x1 = {x1} \n x2 = {x2}")