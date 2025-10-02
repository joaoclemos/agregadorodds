# backend/scraper.py (VERSÃO FINAL PARA TESTE)

import requests
from bs4 import BeautifulSoup
import os

# --- CONFIGURAÇÃO ---
# A URL exata do jogo que você escolheu.
URL_ALVO = "https://www.flashscore.com.br/jogo/futebol/barcelona-SKbpVP5K/psg-CjhkPw0k/"

# Cabeçalhos para simular um navegador.
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def main():
    """
    Função principal que raspa os dados da página específica do jogo.
    """
    print("--- INICIANDO O ROBÔ SCRAPER (VERSÃO DE TESTE) ---")
    
    print(f"Baixando o conteúdo de: {URL_ALVO}")
    try:
        # Faz a requisição para obter o HTML da página
        response = requests.get(URL_ALVO, headers=HEADERS)
        # Verifica se a página foi encontrada e baixada com sucesso
        response.raise_for_status() 
    except requests.exceptions.RequestException as e:
        print(f"Não foi possível acessar a página. Erro: {e}")
        return

    print("Página baixada com sucesso!")
    
    # Usa o BeautifulSoup para "entender" o HTML
    soup = BeautifulSoup(response.content, 'html.parser')

    # --- INÍCIO DO TRABALHO DE DETETIVE ---
    # Com base na estrutura do Flashscore, vamos procurar os elementos.
    
    # 1. Encontra o "container" que guarda as informações do time da casa.
    home_team_container = soup.find('div', class_='duelParticipant__home')
    # 2. Encontra o "container" que guarda as informações do time de fora.
    away_team_container = soup.find('div', class_='duelParticipant__away')

    # 3. Verifica se os dois containers foram encontrados.
    if not home_team_container or not away_team_container:
        print("Não foi possível encontrar os containers dos times. O layout do site pode ter mudado.")
        print("Verifique com F12 as classes 'duelParticipant__home' e 'duelParticipant__away'.")
        return

    # 4. Dentro de cada container, encontra a tag com o nome do time.
    #    Baseado na sua investigação, a classe é 'participant__participantName'.
    time_casa_tag = home_team_container.find('a', class_='participant__participantName')
    time_fora_tag = away_team_container.find('a', class_='participant__participantName')
    
    # 5. Verifica se as tags com os nomes foram encontradas.
    if time_casa_tag and time_fora_tag:
        # Se encontrou, extrai o texto de dentro delas.
        time_casa = time_casa_tag.text.strip()
        time_fora = time_fora_tag.text.strip()
        
        print("\n" + "="*30)
        print("  DADOS ENCONTRADOS COM SUCESSO!")
        print("="*30)
        print(f"  Time da Casa: {time_casa}")
        print(f"  Time de Fora: {time_fora}")
        print("="*30)
        
        # Futuramente, aqui chamaremos a função para salvar no banco de dados.
        
    else:
        print("Nomes dos times não encontrados dentro dos containers.")
        print("Verifique com F12 a classe 'participant__participantName'.")

if __name__ == "__main__":
    main()