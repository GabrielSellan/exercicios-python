
from app import conectar

conn = conectar()
cursor = conn.cursor()

movies = ["Homen Aranha", "JackAss", "A volta dos que não foram"]


def mediaNotas():
    cursor.execute("select filme, count(*), sum(nota) from filme_nota group by filme;")
    result = cursor.fetchall()

    print("Filmes com média de avaliação maior que 6: ")
    for i in result:
        media = i[2] / i[1]
        if media > 6:
            print(f"{i[0]} com média: {media}")


print(f"Temos {len(movies)} filmes para você avaliar")
for i in movies:
    print(f"Avalie {i} de 0 á 10:")
    nota = input("Sua nota: ")

    cursor.execute("insert into filme_nota (filme, nota) values (%s, %s)", (i, nota,))
    conn.commit()


mediaNotas()


cursor.close()
conn.close()
