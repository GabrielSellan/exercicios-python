from app import conectar

conn = conectar()
cursor = conn.cursor()



while True:
    

    op = input("Digite 'C' para adicionar um cliente ou 'P' para parar: ")

    if op == 'P':
        break


    if op != 'C':
        print("Input não aceito!")
    else:
        nome = input("Nome do cliente: ")
        idade = int(input("Idade do cliente: "))
        altura = float(input("Altura do cliente: "))

        cursor.execute("insert into customer (nome) value (%s)",(nome,))
        conn.commit()

        cursor.execute("insert into customer_info (idade, altura) value (%s,%s)",(idade, altura,))
        conn.commit()


cursor.execute("select c.nome, ci.idade, ci.altura from customer c join customer_info ci on c.id = ci.id")
clienteCompleto = cursor.fetchall()


print("Clintes inseridos com suas infos: ")
for i in clienteCompleto:
    print(f"{i[0]} - {i[1]} - {i[2]}")



cursor.close()
conn.close()



