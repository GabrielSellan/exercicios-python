
import datetime

ano_nascimento = int(input("Informe seu ano de nascimento: "))
ano_atual = int(datetime.date.today().year)

idade = ano_atual - ano_nascimento

if idade <= 19:
    print("Joven")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")