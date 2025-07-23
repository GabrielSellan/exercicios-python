from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
import requests
import datetime
from app import conectar

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = ""


def busca_registro(handler, c):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT nome, temperatura FROM clima WHERE nome = %s ORDER BY date DESC LIMIT 1;", (c,))
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    cidade, temperatura = result[0]

    resposta = f"""
                <html><body>
                    <h2>Informações: </h2>
                    <p>Cidade: {cidade}</p>
                    <p>Temperatura: {temperatura}</p>
                    <a href="/cidade">Voltar</a>
                </body></html>
            """
    handler.send_response(400)
    handler.send_header('Content-type', 'text/html')
    handler.end_headers()
    handler.wfile.write(resposta.encode('utf-8'))
    return



class FormHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/cidade':
            html = """
                <html>
                    <body>
                        <h2>Clima da cidade</h2>
                        <form method="post" action="/submit">
                            Cidade: <input type="text" name="cidade"><br><br>
                            <input type="submit" value="Enviar">
                        </form>
                    </body>
                </html>
            """
            self.respond(html.encode('utf-8'))
        else:
            self.send_error(404, "Página não encontrada.")

    def do_POST(self):
        cidade = ""
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            campos = parse_qs(post_data)

            cidade = campos.get("cidade", [""])[0]
        else:
            self.send_error(404, "Endpoint POST não encontrado.")


        url = BASE_URL + "appid=" + API_KEY + "&q=" + cidade
        resposta = requests.get(url).json()

        temperatura = resposta['main']['temp'] - 273.15
        data = datetime.datetime.fromtimestamp(resposta['dt']).strftime("%Y-%m-%d")

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("insert into clima (nome, temperatura, date) value (%s,%s,%s)", (cidade, temperatura, data,))
        conn.commit()

        cursor.close()
        conn.close()

        busca_registro(self, cidade)

    def respond(self, content):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(content)


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, FormHandler)
    print("Servidor rodando em http://localhost:8000")
    httpd.serve_forever()