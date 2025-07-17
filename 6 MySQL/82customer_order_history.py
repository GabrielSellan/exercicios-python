from app import conectar
from datetime import date

conn = conectar()
cursor = conn.cursor()

def addOrder(o, i, d):
    cursor.execute("insert into orders (order_title,customer_id, data) value (%s,%s,%s)", (o, i, d,))
    conn.commit()

    cursor.execute("select order_title, data from orders where customer_id = %s", (i,))
    result = cursor.fetchall()

    print("\nSeu historico de pedidos: ")
    for i in result:
        print(f"{i[0]} - {i[1]}")


print("Adicionar pedido: ")
id = int(input("Informe se Id: "))
order = input("Titulo do pedido: ")
data = date.today().strftime("%Y-%m-%d")

addOrder(order, id, data)



cursor.close()
conn.close()