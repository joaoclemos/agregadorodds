# backend/app.py

import sqlite3
from flask import Flask, jsonify
from flask_cors import CORS # <-- NOVA LINHA 1: Importa a ferramenta CORS
import os

# --- CONFIGURAÇÃO ---
app = Flask(__name__)
CORS(app) # <-- NOVA LINHA 2: Ativa o CORS para toda a sua aplicação

DB_FOLDER = os.path.join("backend", "database")
DB_NAME = os.path.join(DB_FOLDER, "checkodds.db")

# --- FUNÇÃO AUXILIAR ---
def get_db_connection():
    """Cria uma conexão com o banco de dados."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# --- CRIAÇÃO DA ROTA DA API ---
@app.route('/api/jogos')
def get_jogos():
    """Busca os jogos no banco de dados e os retorna em formato JSON."""
    print("Requisição recebida na rota /api/jogos")
    
    conn = get_db_connection()
    jogos_db = conn.execute('SELECT * FROM events').fetchall()
    conn.close()
    
    jogos = [dict(row) for row in jogos_db]
    
    print(f"Encontrados {len(jogos)} jogos no banco. Enviando como resposta.")
    
    return jsonify(jogos)

# --- PONTO DE ENTRADA PARA RODAR O SERVIDOR ---
if __name__ == '__main__':
    app.run(debug=True)