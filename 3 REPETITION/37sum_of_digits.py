
soma = 0
while True:
    num = float(input("Digite um número ou 0 para somar: ")) 
    if num == 0:
        print(f"Sua soma deu: {soma}")
        break
    
    soma += num

