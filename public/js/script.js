// public/js/script.js

// Aguarda o documento HTML ser completamente carregado
document.addEventListener('DOMContentLoaded', () => {
    console.log("JavaScript carregado com sucesso!");

    // Exemplo de como pegaríamos botões de filtro no futuro
    const filterButtons = document.querySelectorAll('.filter-btn');

    // Para cada botão, adiciona um "ouvinte" de clique
    filterButtons.forEach(button => {
        button.addEventListener('click', () => {
            
            // Remove a classe 'active' de todos os botões
            filterButtons.forEach(btn => btn.classList.remove('active'));

            // Adiciona a classe 'active' apenas no botão que foi clicado
            button.classList.add('active');

            console.log(`Filtro "${button.innerText}" selecionado.`);
        });
    });
});