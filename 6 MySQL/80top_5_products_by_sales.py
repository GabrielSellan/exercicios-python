from app import conectar

conn = conectar()
cursor = conn.cursor()

def manipulandoProds():
    cursor.execute("select produto, sum(valor) from vendas group by produto order by sum(valor) desc limit 5")
    prodTotSales = cursor.fetchall()

    sum = 1
    for i in prodTotSales:
        print(f"{sum}° {i[0]} - R${i[1]}")
        sum += 1


manipulandoProds()

cursor.close()
conn.close()
