import sqlite3

# O nome do arquivo do nosso banco de dados
DB_NAME = "checkodds.db"

# SQL para criar as tabelas. O "IF NOT EXISTS" garante que não teremos erro se o script for executado mais de uma vez.
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
    """
    Cria o arquivo do banco de dados e as tabelas necessárias.
    """
    try:
        # sqlite3.connect() cria o arquivo do banco de dados se ele não existir
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        print(f"Banco de dados '{DB_NAME}' conectado com sucesso.")

        # Executa cada um dos comandos SQL para criar as tabelas
        for sql_command in SQL_CREATE_TABLES:
            cursor.execute(sql_command)
        
        print("Tabelas 'bookmakers', 'events' e 'odds' verificadas/criadas com sucesso!")

        # conn.commit() salva as alterações
        conn.commit()

    except sqlite3.Error as e:
        print(f"Ocorreu um erro ao criar o banco de dados: {e}")
    finally:
        # conn.close() fecha a conexão com o banco de dados
        if conn:
            conn.close()
            print("Conexão com o banco de dados fechada.")

# Esta parte do código só será executada quando você rodar o script diretamente
if __name__ == "__main__":
    create_database()