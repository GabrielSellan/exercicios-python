from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from app import conectar



def valida_e_registra(handler, n, e, s):
    conn = conectar()
    cursor = conn.cursor()

    # Pega emails do banco de dados
    cursor.execute("SELECT email FROM registros")
    emails = cursor.fetchall()

    # Validar se email já foi cadastrado
    for i in emails:
        if e == i[0]:
            resposta = """
                <html><body>
                    <h2>Erro no cadastro</h2>
                    <p>Email ja registrado!</p>
                    <a href="/cadastro">Voltar</a>
                </body></html>
            """
            handler.send_response(400)
            handler.send_header('Content-type', 'text/html')
            handler.end_headers()
            handler.wfile.write(resposta.encode('utf-8'))
            return
    
    # Análisa se email tem um formato válido
    if "@" not in e and "." not in e:
        resposta = """
            <html><body>
                <h2>Erro no cadastro</h2>
                <p>Email inválido!</p>
                <a href="/cadastro">Voltar</a>
            </body></html>
        """
        handler.send_response(400)
        handler.send_header('Content-type', 'text/html')
        handler.end_headers()
        handler.wfile.write(resposta.encode('utf-8'))
        return
        
    # Análisa força da senha
    if len(s) < 6:
        resposta = """
            <html><body>
                <h2>Erro no cadastro</h2>
                <p>Senha deve ter mais de 6 digitos</p>
                <a href="/cadastro">Voltar</a>
            </body></html>
        """
        handler.send_response(400)
        handler.send_header('Content-type', 'text/html')
        handler.end_headers()
        handler.wfile.write(resposta.encode('utf-8'))
        return    


    # Insere cadastro válido na tabela 
    cursor.execute("INSERT INTO registros (nome, email, senha) VALUES (%s,%s,%s)", (n,e,s))
    conn.commit()

    resposta = """
        <html><body>
            <h2>Cadastro realizado com sucesso</h2>
            <a href="/cadastro">Voltar</a>
        </body></html>
    """
    handler.send_response(200)
    handler.send_header('Content-type', 'text/html')
    handler.end_headers()
    handler.wfile.write(resposta.encode('utf-8'))
    
    cursor.close()
    conn.close()

            


class FormHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/cadastro':
            html = """
                <html>
                    <body>
                        <h2>Formulario de Teste</h2>
                        <form method="post" action="/submit">
                            Nome: <input type="text" name="nome"><br><br>
                            Email: <input type="email" name="email"><br><br>
                            Senha: <input type="password" name="senha"><br><br>
                            <input type="submit" value="Enviar">
                        </form>
                    </body>
                </html>
            """
            self.respond(html.encode('utf-8'))
        else:
            self.send_error(404, "Página não encontrada.")

    def do_POST(self):
        if self.path == '/submit':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            campos = parse_qs(post_data)

            nome = campos.get("nome", [""])[0]
            email = campos.get("email", [""])[0]
            senha = campos.get("senha", [""])[0]

            valida_e_registra(self, nome, email, senha)

        else:
            self.send_error(404, "Endpoint POST não encontrado.")

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

