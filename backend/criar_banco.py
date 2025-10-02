# backend/criar_banco.py

import sqlite3
import os

# Define a estrutura de pastas e o nome do arquivo
DB_FOLDER = os.path.join("backend", "database")
DB_NAME = os.path.join(DB_FOLDER, "checkodds.db")

# SQL para criar as tabelas
SQL_CREATE_TABLES = [
    """
    CREATE TABLE IF NOT EXISTS bookmakers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        url TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        team_a TEXT NOT NULL,
        team_b TEXT NOT NULL,
        event_date DATETIME NOT NULL,
        league TEXT
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS odds (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        event_id INTEGER NOT NULL,
        bookmaker_id INTEGER NOT NULL,
        market_name TEXT NOT NULL,
        outcome_name TEXT NOT NULL,
        odd_value REAL NOT NULL,
        last_updated DATETIME NOT NULL,
        FOREIGN KEY (event_id) REFERENCES events (id),
        FOREIGN KEY (bookmaker_id) REFERENCES bookmakers (id)
    );
    """
]

def create_database():
    """Cria a estrutura de pastas e o banco de dados com as tabelas."""
    try:
        os.makedirs(DB_FOLDER, exist_ok=True)
        
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        print(f"Banco de dados '{DB_NAME}' conectado/criado com sucesso.")

        for sql_command in SQL_CREATE_TABLES:
            cursor.execute(sql_command)
        
        print("Tabelas verificadas/criadas com sucesso!")
        conn.commit()

    except sqlite3.Error as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if conn:
            conn.close()
            print("Conexão com o banco de dados fechada.")

if __name__ == "__main__":
    create_database()