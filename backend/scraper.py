# backend/scraper.py (VERSÃO FINAL: Raspa e Salva no Banco)

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import os
import sqlite3
from datetime import datetime

# --- CONFIGURAÇÃO ---
URL_ALVO = "https://www.flashscore.com.br/jogo/futebol/barcelona-SKbpVP5K/psg-CjhkPw0k/"
CHROME_DRIVER_PATH = './chromedriver.exe'
DB_FOLDER = os.path.join("backend", "database")
DB_NAME = os.path.join(DB_FOLDER, "checkodds.db")
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# --- FUNÇÕES DO BANCO DE DADOS ---
def conectar_banco():
    """Cria uma conexão com o banco de dados SQLite."""
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def inserir_evento(conn, time_casa, time_fora, data_evento, liga):
    """Insere um novo evento na tabela 'events' do banco de dados."""
    sql = ''' INSERT OR IGNORE INTO events(team_a, team_b, event_date, league)
              VALUES(?,?,?,?) '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (time_casa, time_fora, data_evento, liga))
        conn.commit()
        return cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Erro ao inserir evento: {e}")
        return None

# --- FUNÇÃO PRINCIPAL ---
def main():
    """
    Função principal que raspa os dados e os salva no banco.
    """
    print("--- INICIANDO O ROBÔ SCRAPER (VERSÃO FINAL) ---")
    
    service = Service(executable_path=CHROME_DRIVER_PATH)
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={HEADERS["User-Agent"]}')
    
    driver = webdriver.Chrome(service=service, options=options)
    print(f"Acessando a página: {URL_ALVO}")

    try:
        driver.get(URL_ALVO)
        print("Aguardando 5 segundos para o JavaScript carregar...")
        time.sleep(5)

        page_content = driver.page_source
        soup = BeautifulSoup(page_content, 'html.parser')

        home_team_container = soup.find('div', class_='duelParticipant__home')
        away_team_container = soup.find('div', class_='duelParticipant__away')

        if home_team_container and away_team_container:
            time_casa_tag = home_team_container.find('a', class_='participant__participantName')
            time_fora_tag = away_team_container.find('a', class_='participant__participantName')
            
            if time_casa_tag and time_fora_tag:
                time_casa = time_casa_tag.text.strip()
                time_fora = time_fora_tag.text.strip()
                
                print(f"Dados encontrados: {time_casa} vs {time_fora}")

                # --- AGORA ESTAMOS SALVANDO NO BANCO DE DADOS ---
                print("\nSalvando dados no banco...")
                conn = conectar_banco()
                if conn:
                    # Usando a data e hora atuais apenas como exemplo
                    data_do_jogo = datetime.now() 
                    liga_do_jogo = "Champions League (Exemplo)"

                    evento_id = inserir_evento(conn, time_casa, time_fora, data_do_jogo, liga_do_jogo)
                    if evento_id:
                        print(f"SUCESSO! Jogo salvo no banco de dados com o ID: {evento_id}")
                    else:
                        # Se o ID não for retornado, é porque o 'INSERT OR IGNORE' pulou a inserção
                        print("AVISO: O jogo já existia no banco de dados e não foi inserido novamente.")
                    conn.close()
                    print("Conexão com o banco de dados fechada.")
                # --- FIM DO TRECHO DE SALVAR ---
                
            else:
                print("ERRO: Nomes dos times não encontrados dentro dos containers.")
        else:
            print("ERRO: Containers dos times não encontrados na página.")

    finally:
        driver.quit()
        print("Navegador fechado.")


if __name__ == "__main__":
    main()