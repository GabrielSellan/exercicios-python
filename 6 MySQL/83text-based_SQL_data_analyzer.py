from app import conectar
import csv

conn = conectar()
cursor = conn.cursor()



def dataAna():
    print(f"Você registrou {orders} pedidos!")
    cursor.execute(f"select * from orders order by id desc limit {orders}")
    result = cursor.fetchall()
    for i in result[::-1]:
        print(f"{i[0]} - {i[1]} - {i[2]}")

with open('ex.csv', mode='r', newline='', encoding='utf-8') as arquivo:
    
    leitor = csv.reader(arquivo)
    orders = 0

    i = 0
    for l in leitor:
        if i == 0:
            i += 1
        else:
            cursor.execute("insert into orders (order_title,customer_id, data) value (%s,%s,%s)", (l[0], l[1], l[2],))
            conn.commit()
            orders += 1

    dataAna()


cursor.close()
conn.close()