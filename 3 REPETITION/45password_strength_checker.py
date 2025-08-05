
senha = input("Digite sua senha: ")
forca = " "
resumo = ""

#Analisa se tem + de 8 caracteres
if len(senha) >= 8:
    forca += "*"
    resumo += "Sua senha tem 8 digitos ou mais (+1)\n"
else:
    resumo += "Sua senha tem menos de 8 digitos\n"

#Analisa se tem letras maiusculas
uppers = 0
for i in senha:
    if i.isupper():
        uppers += 1

if uppers > 0:
    forca += "*"
    resumo += " Sua senha tem caracteres maiusculos (+1)\n"
else:
    resumo += " Sua senha não possui caracteres maiusculos\n"

#Analisa se tem letras minusculas
lowers = 0
for i in senha:
    if i.islower():
        lowers += 1

if lowers > 0:
    forca += "*"
    resumo += " Sua senha tem caracteres minusculos (+1)\n"
else:
    resumo += " Sua senha não possui caracteres minusculos\n"

#Analisa se tem números
numerico = False
for i in senha:
    if i.isnumeric():
        numerico = True
    
if numerico:
    forca += "*"
    resumo += " Sua senha tem números (+1)\n" 
else:
    resumo += " Sua senha não tem números\n"

#Analisa simbolos
simbo = False
for i in senha:
    if i.isalnum():
        simbo = True
    
if simbo:
    forca += "*"
    resumo += " Sua senha tem simbolos (+1)\n" 
else:
    resumo += " Sua senha não tem simbolos\n"


print(f"Resumo da sua senha:\n {resumo}")
print(f"Força da sua senha: {forca}")