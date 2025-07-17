from app import conectar

conn = conectar()
cursor = conn.cursor()

def checkEmail(e):
    
    cursor.execute("SELECT email FROM registros")
    emails = cursor.fetchall()

    for i in emails:
        if e == i[0]:
            print("Email já registrado!")
            return False
    
    return True

def register(n, e, s):
    infoCheck = True

    if "@" in e and "." in e:
        pass
    else:
        infoCheck = False

    if len(s) < 6:
        infoCheck = False
    
    if infoCheck == True and checkEmail(e):
        cursor.execute("INSERT INTO registros (nome, email, senha) VALUES (%s,%s,%s)", (n,e,s))
        conn.commit()
    


nome = input("Nome: ")
email = input("Email: ")
senha = input("Senha: ")

register(nome,email,senha)

cursor.close()
conn.close()