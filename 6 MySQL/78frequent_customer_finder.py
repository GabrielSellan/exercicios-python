from app import conectar

conn = conectar()
cursor = conn.cursor()

def clienteFrequente():
    
    cursor.execute("select nome, count(*) from customer group by nome having count(*) > 1;")
    resultado = cursor.fetchall()
    
    return resultado

clienteFrequente()

cursor.close()
conn.close()
