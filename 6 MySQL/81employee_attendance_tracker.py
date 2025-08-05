from app import conectar
from datetime import date

conn = conectar()
cursor = conn.cursor()


def registerEmp(id):
    dataDeHoje = date.today().strftime('%Y-%m-%d')

    cursor.execute(f"select name from employees where id = {id};")
    empName = cursor.fetchall()

    cursor.execute("INSERT INTO attendance (employee_id, date, present) VALUES (%s, %s, %s)",(id, dataDeHoje, 1))
    conn.commit()

    print(f"Registro realizado com sucesso {empName}")


def regisEmpFalta():

    cursor.execute("SELECT employee_id, COUNT(*) AS faltas FROM attendance WHERE present = 0 GROUP BY employee_id HAVING COUNT(*) > 1;")
    result = cursor.fetchall()

    print("Funcionários com mais de 1 falta: ")
    for i in result:

        cursor.execute(f"select name from employees where id = {i[0]};")
        name = cursor.fetchall()

        print(f"{name} teve {i[1]} faltas")



empRegi = input("Informe seu id para registro: ")
registerEmp(empRegi)
regisEmpFalta()






cursor.close()
conn.close()
