import random

num = random.randint(1, 100)

chute = 0
while chute != num:
    chute = int(input("Qual seu palpite entre 1 e 100? "))
    if chute == num:
        print("Você acertou!")
    elif chute < num:
        print("Muito baixo v\n")
    else:
        print("Muito alto ^\n") 
