#A=P×(1+r)^t

#A é o montante final (principal + juros),
#P é o valor principal (o valor inicial do investimento ou empréstimo),
#r é a taxa de juros por período (expressa como um valor decimal),
#t é o número de períodos (geralmente, em anos).

p = float(input("Informe o valor principal: "))
r = float(input("Informe a taxa de juros em %: ")) / 100
t = float(input("Informe o periodo em anos: "))

a = p * ((1 + r)**t)

print(f"O juro composto será de R${a - p:.2f}")