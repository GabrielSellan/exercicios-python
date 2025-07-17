import time

num = int(input("Digite um numero de segundos: "))

for i in range(1, num + 1):
    time.sleep(2)
    print(i)
    