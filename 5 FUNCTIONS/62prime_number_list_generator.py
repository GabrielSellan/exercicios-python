import math

listaPrimos = []

def primeNum(a):
    for i in range(2, int(a) + 1):
        primo = True
        for y in range(2, int(a) + 1):
            if i % y == 0 and y != i:
                primo = False     
        if primo == True:
            listaPrimos.append(i)    
            
num = int(input("Informe um número: "))
primeNum(num)

print(f"Essa é a lista de primos até {num}: {listaPrimos}")