
char = input("Informe um caractere: ")

if char.isalpha():
    if char.lower() in 'aeiou':
        print("É uma vogal.")
    else:
        print("É uma consoante.")
elif char.isdigit():
    print("É um dígito.")
else:
    print("É um caractere especial.")

