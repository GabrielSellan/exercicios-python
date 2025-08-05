from flask import Flask, request, jsonify
from app import conectar  # mesma função que você já tem

app = Flask(__name__)


# GET: listar produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome, preco, quantidade FROM inventario;")
    produtos = cursor.fetchall()
    cursor.close()
    conn.close()

    return jsonify([
        {"nome": n, "preco": float(p), "quantidade": q}
        for (n, p, q) in produtos
    ])


# POST: adicionar produto
@app.route('/produtos', methods=['POST'])
def adicionar_produto():
    dados = request.get_json()

    nome = dados.get("nome")
    preco = dados.get("preco")
    quantidade = dados.get("quantidade")

    if not nome or preco is None or quantidade is None:
        return jsonify({"erro": "Campos obrigatórios ausentes"}), 400

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM inventario WHERE nome = %s;", (nome,))
    existe = cursor.fetchone()

    if existe:
        cursor.close()
        conn.close()
        return jsonify({"erro": "Produto já existe"}), 409

    cursor.execute("INSERT INTO inventario (nome, preco, quantidade) VALUES (%s, %s, %s);", (nome, preco, quantidade))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensagem": "Produto adicionado"}), 201


# PUT: editar produto
@app.route('/produtos/<nome>', methods=['PUT'])
def editar_produto(nome):
    dados = request.get_json()
    preco = dados.get("preco")
    quantidade = dados.get("quantidade")

    if preco is None or quantidade is None:
        return jsonify({"erro": "Campos obrigatórios ausentes"}), 400

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE inventario SET preco = %s, quantidade = %s WHERE nome = %s;", (preco, quantidade, nome))
    
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"erro": "Produto não encontrado"}), 404

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"mensagem": "Produto atualizado"})


# DELETE: remover produto (opcional)
@app.route('/produtos/<nome>', methods=['DELETE'])
def deletar_produto(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM inventario WHERE nome = %s;", (nome,))
    
    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"erro": "Produto não encontrado"}), 404

    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({"mensagem": "Produto removido"})


if __name__ == '__main__':
    app.run(debug=True)
