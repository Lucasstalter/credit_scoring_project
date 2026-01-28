// API Configuration
const API_URL = 'https://creditscoringproject-production.up.railway.app';

// Fill sample data
function fillSampleData() {
    document.getElementById('customer_id').value = 'CLI001';
    document.getElementById('idade').value = '35';
    document.getElementById('renda_mensal').value = '5000.00';
    document.getElementById('divida_total').value = '15000.00';
    document.getElementById('limite_credito').value = '10000.00';
    document.getElementById('saldo_utilizado').value = '7000.00';
    document.getElementById('valor_parcela').value = '500.00';
    document.getElementById('idade_credito_meses').value = '60';
    document.getElementById('tempo_emprego_meses').value = '24';
    document.getElementById('atrasos_30d').value = '1';
    document.getElementById('atrasos_90d').value = '0';
    document.getElementById('pagamentos_dia').value = '11';
    document.getElementById('renda_std_6m').value = '200.00';
}

// Format currency
function formatCurrency(value) {
    return new Intl.NumberFormat('pt-BR', {
        style: 'currency',
        currency: 'BRL'
    }).format(value);
}

// Format timestamp
function formatTimestamp(timestamp) {
    const date = new Date(timestamp);
    return date.toLocaleString('pt-BR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Reset form
function resetForm() {
    document.getElementById('creditForm').reset();
    hideResult();
    hideError();
    document.getElementById('creditForm').style.display = 'block';
    
    // Scroll to form
    const demoSection = document.getElementById('demo');
    demoSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

// Show/hide states
function showLoading() {
    document.getElementById('creditForm').style.display = 'none';
    document.getElementById('loading').style.display = 'block';
    hideResult();
    hideError();
}

function hideLoading() {
    document.getElementById('loading').style.display = 'none';
}

function showResult(data) {
    hideLoading();
    
    const resultCard = document.getElementById('resultCard');
    const statusIndicator = document.querySelector('.status-indicator');
    const statusText = document.getElementById('statusText');
    
    // Update status
    if (data.approved) {
        statusIndicator.classList.remove('rejected');
        statusIndicator.classList.add('approved');
        statusText.textContent = 'Aprovado';
    } else {
        statusIndicator.classList.remove('approved');
        statusIndicator.classList.add('rejected');
        statusText.textContent = 'Negado';
    }
    
    // Update score
    const scorePercentage = (data.score * 100).toFixed(1);
    document.getElementById('scoreValue').textContent = scorePercentage + '%';
    
    // Update metrics
    document.getElementById('metricCustomer').textContent = data.customer_id;
    document.getElementById('metricCategory').textContent = data.risk_category;
    document.getElementById('metricLimit').textContent = data.limit_recommended 
        ? formatCurrency(data.limit_recommended) 
        : 'R$ 0,00';
    document.getElementById('metricTimestamp').textContent = formatTimestamp(data.timestamp);
    
    // Update risk bar
    document.getElementById('riskBarFill').style.width = scorePercentage + '%';
    
    // Show result card
    resultCard.style.display = 'block';
    
    // Scroll to result
    setTimeout(() => {
        resultCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }, 100);
}

function hideResult() {
    document.getElementById('resultCard').style.display = 'none';
}

function showError(message) {
    hideLoading();
    
    const errorCard = document.getElementById('errorCard');
    document.getElementById('errorMessage').textContent = message;
    errorCard.style.display = 'block';
    
    // Scroll to error
    setTimeout(() => {
        errorCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
    }, 100);
}

function hideError() {
    document.getElementById('errorCard').style.display = 'none';
    document.getElementById('creditForm').style.display = 'block';
}

// Form submission
document.getElementById('creditForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    // Collect form data
    const formData = {
        customer_id: document.getElementById('customer_id').value,
        idade: parseInt(document.getElementById('idade').value),
        renda_mensal: parseFloat(document.getElementById('renda_mensal').value),
        divida_total: parseFloat(document.getElementById('divida_total').value),
        limite_credito: parseFloat(document.getElementById('limite_credito').value),
        saldo_utilizado: parseFloat(document.getElementById('saldo_utilizado').value),
        valor_parcela: parseFloat(document.getElementById('valor_parcela').value),
        idade_credito_meses: parseInt(document.getElementById('idade_credito_meses').value),
        tempo_emprego_meses: parseInt(document.getElementById('tempo_emprego_meses').value),
        atrasos_30d: parseInt(document.getElementById('atrasos_30d').value),
        atrasos_90d: parseInt(document.getElementById('atrasos_90d').value),
        pagamentos_dia: parseInt(document.getElementById('pagamentos_dia').value),
        renda_std_6m: parseFloat(document.getElementById('renda_std_6m').value)
    };
    
    // Show loading
    showLoading();
    
    try {
        // Call API
        const response = await fetch(`${API_URL}/predict`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        
        if (!response.ok) {
            const errorData = await response.json().catch(() => ({}));
            throw new Error(errorData.detail || `Erro na API: ${response.status}`);
        }
        
        const data = await response.json();
        showResult(data);
        
    } catch (error) {
        console.error('Erro:', error);
        showError(
            error.message || 
            'Não foi possível conectar à API. Verifique se o servidor está rodando em ' + API_URL
        );
    }
});

// Input validations
document.getElementById('idade').addEventListener('input', function() {
    // Permite apenas números
    this.value = this.value.replace(/[^0-9]/g, '');
});

document.getElementById('idade').addEventListener('blur', function() {
    // Valida no blur (quando sair do campo)
    let value = parseInt(this.value);
    if (value < 18) this.value = 18;
    if (value > 100) this.value = 100;
});
document.getElementById('pagamentos_dia').addEventListener('input', function() {
    if (this.value < 0) this.value = 0;
    if (this.value > 12) this.value = 12;
});

document.querySelectorAll('#atrasos_30d, #atrasos_90d').forEach(input => {
    input.addEventListener('input', function() {
        if (this.value < 0) this.value = 0;
    });
});

// Format currency inputs on blur
document.querySelectorAll('input[type="number"][step="0.01"]').forEach(input => {
    input.addEventListener('blur', function() {
        if (this.value) {
            this.value = parseFloat(this.value).toFixed(2);
        }
    });
});

// Smooth scroll for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// Log API configuration
console.log('Credit Scoring Frontend initialized');
console.log('API URL:', API_URL);


// Progress Bar
function updateScrollProgress() {
    const scrollProgress = document.getElementById('scrollProgress');
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const scrollHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    const scrollPercent = (scrollTop / scrollHeight) * 100;
    scrollProgress.style.width = scrollPercent + '%';
}

// Back to Top Button
function updateBackToTopButton() {
    const backToTop = document.getElementById('backToTop');
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    
    if (scrollTop > 300) {
        backToTop.classList.add('visible');
    } else {
        backToTop.classList.remove('visible');
    }
}

// Back to Top Click
document.getElementById('backToTop').addEventListener('click', function() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});

// Scroll Event Listener
let scrollTimeout;
window.addEventListener('scroll', function() {
    updateScrollProgress();
    updateBackToTopButton();
    
    // Debounce for performance
    clearTimeout(scrollTimeout);
    scrollTimeout = setTimeout(function() {
        checkFadeInElements();
    }, 50);
});

// Fade In on Scroll
function checkFadeInElements() {
    const fadeElements = document.querySelectorAll('.fade-in');
    const windowHeight = window.innerHeight;
    
    fadeElements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const elementVisible = 150; // Distance from viewport before fade in
        
        if (elementTop < windowHeight - elementVisible) {
            element.classList.add('visible');
        }
    });
}

// Add fade-in class to elements
function initFadeInElements() {
    // Add to feature cards
    document.querySelectorAll('.feature-card').forEach(card => {
        card.classList.add('fade-in');
    });
    
    // Add to stats
    document.querySelectorAll('.stat').forEach(stat => {
        stat.classList.add('fade-in');
    });
    
    // Add to form sections
    document.querySelectorAll('.form-section').forEach(section => {
        section.classList.add('fade-in');
    });
    
    // Initial check
    checkFadeInElements();
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    initFadeInElements();
    updateScrollProgress();
    updateBackToTopButton();
});

// Smooth scroll for anchor links (already exists, but ensuring it works)
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            const offsetTop = target.offsetTop - 80; // Account for sticky nav
            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        }
    });
});

console.log('Scroll enhancements initialized');