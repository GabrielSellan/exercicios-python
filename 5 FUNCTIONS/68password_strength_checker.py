import string
import os

senhas = []

def checkSenha(s):
    senhaForte = True
    aviso = []

    if len(s) < 6:
        senhaForte = False
        aviso.append("Senha com menos de 6 caracteres")
    
    if not any(char.isdigit() for char in s):
        senhaForte = False
        aviso.append("Senha não contem números")

    if not any(char.isupper() for char in s):
        senhaForte = False
        aviso.append("Senha não possui letras maiusculas")

    if not any(char in string.punctuation for char in s):
        senhaForte = False
        aviso.append("Senha não possui caracter especial")

    if senhaForte == True:
        os.system('cls')
        print("Senha aceita!!!")

        if len(senhas) > 0:
            print("Suas tentativas:\n")
            for i in senhas:
                print(i)
        return False
    else:
        os.system('cls')
        for i in aviso:
            print(i)
        print("Tente outra senha")
    
while True:
    senha = input("Digite uma senha forte: ")    
    
    if checkSenha(senha) == False:
        break

    senhas.append(senha)