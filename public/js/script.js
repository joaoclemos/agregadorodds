// public/js/script.js

document.addEventListener('DOMContentLoaded', () => {
    carregarJogos();
});

function carregarJogos() {
    console.log("Iniciando busca por jogos na API...");
    const listaDeJogosContainer = document.getElementById('lista-de-jogos');
    
    // --- CORREÇÃO AQUI ---
    // Fornecemos o endereço completo do nosso servidor Flask
    const apiUrl = 'http://127.0.0.1:5000/api/jogos';

    fetch(apiUrl)
        .then(response => {
            console.log("Resposta da API recebida. Convertendo para JSON...");
            // Se a resposta não for OK (ex: erro 500 no servidor), nós lançamos um erro
            if (!response.ok) {
                throw new Error(`Erro de rede: ${response.statusText}`);
            }
            return response.json();
        })
        .then(jogos => {
            console.log("Dados dos jogos recebidos:", jogos);
            listaDeJogosContainer.innerHTML = '';

            if (jogos.length === 0) {
                listaDeJogosContainer.innerHTML = '<p>Nenhum jogo encontrado no banco de dados. Execute o robô (scraper.py) para buscar os dados.</p>';
                return;
            }

            jogos.forEach(jogo => {
                const jogoHTML = `
                    <div class="game-card">
                        <span class="game-league">${jogo.league}</span>
                        <div class="game-teams">
                            <span class="team-name">${jogo.team_a}</span>
                            <span class="vs">vs</span>
                            <span class="team-name">${jogo.team_b}</span>
                        </div>
                        <span class="game-date">${new Date(jogo.event_date).toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit' })}</span>
                    </div>
                `;
                listaDeJogosContainer.innerHTML += jogoHTML;
            });
        })
        .catch(error => {
            console.error("Erro ao buscar jogos:", error);
            listaDeJogosContainer.innerHTML = '<p>Erro ao carregar os jogos. Verifique se o servidor Python (app.py) está rodando e se não há erros no console.</p>';
        });
}