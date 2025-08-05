
num = int(input("Quantos números que na sequência de fibonacci? "))

f1 = 0
f2 = 1
for i in range(num):
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2