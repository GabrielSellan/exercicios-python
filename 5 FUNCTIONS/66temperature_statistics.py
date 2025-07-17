
temp = []

def addTemp(a):
    temp.append(a)

def aboveMedTemp():
    soma = 0
    for t in temp:
        soma += t

    mediaTemp = soma/len(temp)
    
    aboveTemp = []
    for t in temp:
        if t > mediaTemp:
            aboveTemp.append(f"{t}°C")

    print(f"Temperaturas acima da média({mediaTemp:.2f}°C): {aboveTemp}")

def highLowTemp():
    tempOrg = sorted(temp, reverse=True)
    high = tempOrg[0]
    lowe = tempOrg[-1]
    print(f"Maior temperatura: {high}°C\nMenor temperatura: {lowe}°C")


while True:
    temInput = input("Digite informe a temperatura de um dia ou 'Pare' para parar: ")

    if temInput == "Pare":
        break
    
    tempInt = int(temInput)
    addTemp(tempInt)

aboveMedTemp()
highLowTemp()
