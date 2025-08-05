from flask import Flask, request, jsonify
import datetime
import requests
from app import conectar

app = Flask(__name__)

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = ""


def busca_registro(c):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT temperatura FROM clima WHERE nome = %s ORDER BY date DESC LIMIT 1;", (c,))
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    temperatura = result[0][0]

    if result:
        temperatura = result[0][0]
        return jsonify({
            "nome": c,
            "temperatura": temperatura
        })
    else:
        return jsonify({"erro": "Cidade não encontrada"}), 404



@app.route('/cidade/<nome>', methods=['GET'])
def temp_da_cidade(nome):
    return busca_registro(nome)



@app.route('/cidade/<nome>', methods=['POST'])
def adicionar_info_cidade(nome):
    
    url = BASE_URL + "appid=" + API_KEY + "&q=" + nome

    resposta = requests.get(url).json()

    temperatura = resposta['main']['temp'] - 273.15
    data = datetime.datetime.fromtimestamp(resposta['dt']).strftime("%Y-%m-%d")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("insert into clima (nome, temperatura, date) value (%s,%s,%s)", (nome, temperatura, data,))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensagem": "Dados inseridos com sucesso!"}), 201
     


if __name__ == '__main__':
    app.run(debug=True)