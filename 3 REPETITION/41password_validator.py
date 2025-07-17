
while True:
    valida = False
    senha = input("Insira uma senha com 8 caracteres e um carater especial: ")

    for i in senha:
        if i.isalnum():
            valida = True
        else:
             valida = False    
    
    if len(senha) >= 8:
        valida = True
    else:
        valida = False

    if valida == True:
        print("Senha aceita!")
        break
    else:
        print("Senha não cumpre os critérios tente novamente\n")
    
