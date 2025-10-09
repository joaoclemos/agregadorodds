# backend/scraper.py

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import os

# --- CONFIGURAÇÃO ---
# ATENÇÃO: Cole aqui a URL do JOGO ESPECÍFICO que você quer testar
URL_ALVO = "https://www.flashscore.com.br/jogo/futebol/exemplo-de-jogo/"

# O caminho para o nosso "motorista" do Chrome (deve estar na pasta raiz do projeto)
CHROME_DRIVER_PATH = './chromedriver.exe' 

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def main():
    """
    Função principal que usa o Selenium para carregar a página e o BeautifulSoup para extrair os dados.
    """
    print("--- INICIANDO O ROBÔ SCRAPER (VERSÃO SELENIUM) ---")
    
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
        print("Página completa carregada com sucesso!")
        
        soup = BeautifulSoup(page_content, 'html.parser')

        home_team_container = soup.find('div', class_='duelParticipant__home')
        away_team_container = soup.find('div', class_='duelParticipant__away')

        if not home_team_container or not away_team_container:
            print("Não foi possível encontrar os containers dos times. O layout do site pode ter mudado.")
            return

        time_casa_tag = home_team_container.find('a', class_='participant__participantName')
        time_fora_tag = away_team_container.find('a', class_='participant__participantName')
        
        if time_casa_tag and time_fora_tag:
            time_casa = time_casa_tag.text.strip()
            time_fora = time_fora_tag.text.strip()
            
            print("\n" + "="*30)
            print("  DADOS ENCONTRADOS COM SUCESSO!")
            print("="*30)
            print(f"  Time da Casa: {time_casa}")
            print(f"  Time de Fora: {time_fora}")
            print("="*30)
            
        else:
            print("Nomes dos times não encontrados. Verifique a classe 'participant__participantName'.")

    finally:
        driver.quit()
        print("Navegador fechado.")


if __name__ == "__main__":
    main()