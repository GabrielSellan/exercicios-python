
USER = "admin"
PASSWORD = "0000"

user = input("Informe seu usuário: ")
password = input("Informe sua senha: ")

if user == USER and password == PASSWORD:
    print("Access Granted")
else:
    print("Access Denied")