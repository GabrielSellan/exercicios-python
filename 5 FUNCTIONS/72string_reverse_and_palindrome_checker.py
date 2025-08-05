
lista = []
mss = ["Palavra - Reverso - Palindromo"]

def stringChecks(s): 
    revS = s[::-1]
    
    pali = " "
    if s == revS:
        pali = 'Sim'
    else:
        pali = 'Não'

    mss.append(f"{s}  -  {revS}  -  {pali}")


while True:
    numString = input("Digite um algo ou 'Pare' para parar: ")

    if numString == "Pare":
        break
    
    stringChecks(numString)

    lista.append(numString)


for i in mss:
    print(i)