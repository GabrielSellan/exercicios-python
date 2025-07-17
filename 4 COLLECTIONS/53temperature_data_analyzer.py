

listaTemp = []
listaSem = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo', 'Domingo']
mediaTemp = 0

for i in range(0, 7):
    dayTemp = float(input(f"Informe a temperatura de {listaSem[i]}: "))
    
    listaTemp.append(dayTemp)


for i in listaTemp:
    mediaTemp += i 
mediaTemp = mediaTemp/7


for i in range(0,7):
    print(f"{listaSem[i]} - {listaTemp[i]}°C")
print(f"Média - {mediaTemp:.2f}°C")        



