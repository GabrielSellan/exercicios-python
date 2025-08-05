from app import conectar
import os

conn = conectar()
cursor = conn.cursor()

def searchCustomer(c):
    cursor.execute("SELECT nome FROM customer")
    result = cursor.fetchall()

    for i in result:
        n = i[0].split(" ")
        for j in n:
            if j == c:
                print(i[0])


while True:
    pesq = input("Buscar cliente: ")
    os.system('cls')
    searchCustomer(pesq)


cursor.close()
conn.close()
