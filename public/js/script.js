// DOM Elements
const sportItems = document.querySelectorAll('.sport-item');
const filterButtons = document.querySelectorAll('.filter-btn');
const tabButtons = document.querySelectorAll('.tab-btn');
const oddsElements = document.querySelectorAll('.odd');
const promoCards = document.querySelectorAll('.promo-card');

// Initialize the application
document.addEventListener('DOMContentLoaded', function() {
    initializeSportsMenu();
    initializeFilters();
    initializeTabs();
    initializeOdds();
    initializePromoCards();
    initializeSearch();
    addAnimations();
});

// Sports Menu Functionality
function initializeSportsMenu() {
    sportItems.forEach(item => {
        item.addEventListener('click', function() {
            // Remove active class from all items
            sportItems.forEach(i => i.classList.remove('active'));
            // Add active class to clicked item
            this.classList.add('active');
            
            // Add click animation
            this.style.transform = 'scale(0.98)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
            
            // Simulate loading new content
            loadSportContent(this.querySelector('span').textContent);
        });
    });
}

// Filter Buttons Functionality
function initializeFilters() {
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Remove active class from all buttons
            filterButtons.forEach(b => b.classList.remove('active'));
            // Add active class to clicked button
            this.classList.add('active');
            
            // Add click effect
            this.style.transform = 'scale(0.95)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 150);
        });
    });
}

// Tab Buttons Functionality
function initializeTabs() {
    tabButtons.forEach(tab => {
        tab.addEventListener('click', function() {
            // Remove active class from all tabs
            tabButtons.forEach(t => t.classList.remove('active'));
            // Add active class to clicked tab
            this.classList.add('active');
            
            // Simulate content loading
            const matchesSection = document.querySelector('.matches-section');
            matchesSection.style.opacity = '0.7';
            setTimeout(() => {
                matchesSection.style.opacity = '1';
            }, 300);
        });
    });
}

// Odds Functionality
function initializeOdds() {
    oddsElements.forEach(odd => {
        odd.addEventListener('click', function() {
            // Add to ticket simulation
            addToTicket(this);
            
            // Visual feedback
            this.style.transform = 'scale(1.1)';
            setTimeout(() => {
                this.style.transform = 'scale(1)';
            }, 200);
            
            // Flash effect
            const originalBg = this.style.backgroundColor;
            this.style.backgroundColor = '#4ade80';
            setTimeout(() => {
                this.style.backgroundColor = originalBg;
            }, 300);
        });
        
        // Hover effects
        odd.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05) rotateZ(1deg)';
        });
        
        odd.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1) rotateZ(0deg)';
        });
    });
}

// Promo Cards Functionality
function initializePromoCards() {
    promoCards.forEach(card => {
        // Parallax effect on mouse move
        card.addEventListener('mousemove', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = (y - centerY) / 10;
            const rotateY = (centerX - x) / 10;
            
            this.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.02)`;
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale(1)';
        });
        
        // Click effect for promo buttons
        const promoBtn = card.querySelector('.promo-btn');
        if (promoBtn) {
            promoBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                
                // Create ripple effect
                const ripple = document.createElement('span');
                ripple.classList.add('ripple');
                this.appendChild(ripple);
                
                const rect = this.getBoundingClientRect();
                const size = Math.max(rect.width, rect.height);
                const x = e.clientX - rect.left - size / 2;
                const y = e.clientY - rect.top - size / 2;
                
                ripple.style.cssText = `
                    position: absolute;
                    width: ${size}px;
                    height: ${size}px;
                    left: ${x}px;
                    top: ${y}px;
                    background: rgba(255, 255, 255, 0.3);
                    border-radius: 50%;
                    transform: scale(0);
                    animation: rippleEffect 0.6s linear;
                    pointer-events: none;
                `;
                
                setTimeout(() => {
                    ripple.remove();
                }, 600);
                
                // Simulate action
                showNotification('Promoção reivindicada com sucesso!');
            });
        }
    });
}

// Search Functionality
function initializeSearch() {
    const searchInput = document.querySelector('.search-bar input');
    const searchBtn = document.querySelector('.search-btn');
    
    searchBtn.addEventListener('click', function() {
        const query = searchInput.value.trim();
        if (query) {
            performSearch(query);
        }
    });
    
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            const query = this.value.trim();
            if (query) {
                performSearch(query);
            }
        }
    });
    
    // Auto-complete simulation
    searchInput.addEventListener('input', function() {
        if (this.value.length > 2) {
            // Simulate showing suggestions
            console.log(`Searching for: ${this.value}`);
        }
    });
}

// Add smooth animations
function addAnimations() {
    // Intersection Observer for fade-in animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, observerOptions);
    
    // Observe all major sections
    const sections = document.querySelectorAll('.promo-card, .match-card, .event-item, .upcoming-match');
    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(section);
    });
    
    // Stagger animations for match cards
    const matchCards = document.querySelectorAll('.match-card');
    matchCards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });
}

// Utility Functions
function loadSportContent(sport) {
    console.log(`Loading content for: ${sport}`);
    
    // Simulate loading with a subtle animation
    const mainContent = document.querySelector('.main-content');
    mainContent.style.opacity = '0.8';
    
    setTimeout(() => {
        mainContent.style.opacity = '1';
        showNotification(`Conteúdo de ${sport} carregado!`);
    }, 500);
}

function addToTicket(oddElement) {
    const ticketBadge = document.querySelector('.my-ticket .badge');
    let currentCount = parseInt(ticketBadge.textContent) || 0;
    currentCount++;
    ticketBadge.textContent = currentCount;
    
    // Update ticket content
    const ticketContent = document.querySelector('.ticket-content p');
    if (currentCount === 1) {
        ticketContent.textContent = `${currentCount} aposta selecionada. Continue navegando para adicionar mais apostas!`;
    } else {
        ticketContent.textContent = `${currentCount} apostas selecionadas. Continue navegando para adicionar mais apostas!`;
    }
    
    // Animate badge
    ticketBadge.style.transform = 'scale(1.3)';
    setTimeout(() => {
        ticketBadge.style.transform = 'scale(1)';
    }, 200);
}

function performSearch(query) {
    console.log(`Searching for: ${query}`);
    showNotification(`Buscando por "${query}"...`);
    
    // Simulate search results loading
    setTimeout(() => {
        showNotification(`Resultados encontrados para "${query}"`);
    }, 1000);
}

function showNotification(message) {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = 'notification';
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 20px;
        right: 20px;
        background: linear-gradient(135deg, #4ade80, #22c55e);
        color: white;
        padding: 15px 20px;
        border-radius: 8px;
        font-weight: 600;
        z-index: 1000;
        opacity: 0;
        transform: translateX(100%);
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(74, 222, 128, 0.3);
    `;
    
    document.body.appendChild(notification);
    
    // Show notification
    setTimeout(() => {
        notification.style.opacity = '1';
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Hide notification
    setTimeout(() => {
        notification.style.opacity = '0';
        notification.style.transform = 'translateX(100%)';
        setTimeout(() => {
            notification.remove();
        }, 300);
    }, 3000);
}

// Add CSS for ripple effect
const style = document.createElement('style');
style.textContent = `
    @keyframes rippleEffect {
        to {
            transform: scale(4);
            opacity: 0;
        }
    }
    
    .promo-btn {
        position: relative;
        overflow: hidden;
    }
    
    .notification {
        font-family: inherit;
    }
`;
document.head.appendChild(style);

// Live odds simulation
function simulateLiveOdds() {
    setInterval(() => {
        const odds = document.querySelectorAll('.odd');
        odds.forEach(odd => {
            if (Math.random() > 0.95) { // 5% chance of update
                const currentValue = parseFloat(odd.textContent);
                const change = (Math.random() - 0.5) * 0.2; // ±0.1 change
                const newValue = Math.max(1.01, currentValue + change);
                
                odd.style.background = '#f59e0b'; // Flash yellow
                setTimeout(() => {
                    odd.textContent = newValue.toFixed(2);
                    odd.style.background = ''; // Reset to original
                }, 300);
            }
        });
    }, 5000); // Check every 5 seconds
}

// Initialize live odds simulation
setTimeout(simulateLiveOdds, 2000);