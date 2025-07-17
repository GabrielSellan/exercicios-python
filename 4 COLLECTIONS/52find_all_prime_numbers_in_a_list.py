import math

numInput = []

while True:
    num = int(input("Informe um número ou '00' para parar: "))
    
    if num == 00:
        break

    if num == 2:
        numInput.append(num)
        continue
    
    primo = True
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            primo = False
            break
    
    if primo:
        numInput.append(num)
    
numInput = list(set(numInput))
print(f"Essa é a lista com os números primos que você digitou: {numInput}")