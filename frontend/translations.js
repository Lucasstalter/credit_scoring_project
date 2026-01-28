// translations.js - Internationalization

const translations = {
    pt: {
        // Navigation
        'nav.features': 'Features',
        'nav.demo': 'Demo',
        'nav.api': 'API Docs',
        
        // Hero Section
        'hero.badge': 'Powered by Machine Learning',
        'hero.title.line1': 'Análise de crédito inteligente',
        'hero.title.line2': 'em tempo real',
        'hero.subtitle': 'Sistema de credit scoring baseado em XGBoost com 86.87% de precisão, treinado com 150.000 casos reais para decisões de crédito assertivas.',
        'hero.cta.primary': 'Testar agora',
        'hero.cta.secondary': 'Ver documentação',
        'hero.stats.auc': 'AUC-ROC Score',
        'hero.stats.data': 'Dados de Treino',
        'hero.stats.time': 'Tempo de Resposta',
        
        // Features Section
        'features.title': 'Como funciona',
        'features.subtitle': 'Tecnologia de ponta para decisões de crédito precisas',
        'features.card1.title': 'Modelo XGBoost',
        'features.card1.desc': 'Algoritmo de gradient boosting otimizado com validação cruzada e tuning de hiperparâmetros.',
        'features.card2.title': 'Análise em Tempo Real',
        'features.card2.desc': 'Processamento instantâneo com latência inferior a 100ms para decisões rápidas.',
        'features.card3.title': 'Dados Reais',
        'features.card3.desc': 'Treinado com dataset Kaggle "Give Me Some Credit" contendo 150.000 registros reais.',
        
        // Demo Section
        'demo.title': 'Demonstração',
        'demo.subtitle': 'Preencha os dados abaixo para simular uma análise de crédito',
        
        // Form
        'form.section1': 'Informações Pessoais',
        'form.section2': 'Informações Financeiras',
        'form.section3': 'Histórico de Crédito',
        'form.customer_id': 'ID do Cliente',
        'form.idade': 'Idade',
        'form.renda_mensal': 'Renda Mensal',
        'form.divida_total': 'Dívida Total',
        'form.limite_credito': 'Limite de Crédito',
        'form.saldo_utilizado': 'Saldo Utilizado',
        'form.valor_parcela': 'Valor da Parcela',
        'form.renda_std_6m': 'Volatilidade de Renda',
        'form.idade_credito_meses': 'Idade do Crédito (meses)',
        'form.tempo_emprego_meses': 'Tempo de Emprego (meses)',
        'form.atrasos_30d': 'Atrasos 30-59 dias',
        'form.atrasos_90d': 'Atrasos 90+ dias',
        'form.pagamentos_dia': 'Pagamentos em Dia',
        'form.btn.example': 'Preencher exemplo',
        'form.btn.submit': 'Analisar crédito',
        
        // Result
        'result.approved': 'Aprovado',
        'result.rejected': 'Negado',
        'result.score': 'Score de Risco',
        'result.customer': 'Cliente',
        'result.category': 'Categoria',
        'result.limit': 'Limite Recomendado',
        'result.timestamp': 'Timestamp',
        'result.risk.low': 'Baixo',
        'result.risk.medium': 'Médio',
        'result.risk.high': 'Alto',
        'result.btn.new': 'Nova análise',
        
        // Loading & Error
        'loading.text': 'Processando análise...',
        'error.title': 'Erro ao processar',
        'error.message': 'Ocorreu um erro ao processar sua solicitação.',
        'error.btn': 'Tentar novamente',
        
        // Footer
        'footer.description': 'Sistema de análise de crédito baseado em Machine Learning',
        'footer.copyright': '© 2026 Credit Scoring. Desenvolvido para fins educacionais.'
    },
    
    en: {
        // Navigation
        'nav.features': 'Features',
        'nav.demo': 'Demo',
        'nav.api': 'API Docs',
        
        // Hero Section
        'hero.badge': 'Powered by Machine Learning',
        'hero.title.line1': 'Intelligent credit analysis',
        'hero.title.line2': 'in real-time',
        'hero.subtitle': 'Credit scoring system based on XGBoost with 86.87% accuracy, trained on 150,000 real cases for accurate credit decisions.',
        'hero.cta.primary': 'Try now',
        'hero.cta.secondary': 'View documentation',
        'hero.stats.auc': 'AUC-ROC Score',
        'hero.stats.data': 'Training Data',
        'hero.stats.time': 'Response Time',
        
        // Features Section
        'features.title': 'How it works',
        'features.subtitle': 'Cutting-edge technology for accurate credit decisions',
        'features.card1.title': 'XGBoost Model',
        'features.card1.desc': 'Optimized gradient boosting algorithm with cross-validation and hyperparameter tuning.',
        'features.card2.title': 'Real-Time Analysis',
        'features.card2.desc': 'Instant processing with latency under 100ms for fast decisions.',
        'features.card3.title': 'Real Data',
        'features.card3.desc': 'Trained with Kaggle dataset "Give Me Some Credit" containing 150,000 real records.',
        
        // Demo Section
        'demo.title': 'Demonstration',
        'demo.subtitle': 'Fill in the data below to simulate a credit analysis',
        
        // Form
        'form.section1': 'Personal Information',
        'form.section2': 'Financial Information',
        'form.section3': 'Credit History',
        'form.customer_id': 'Customer ID',
        'form.idade': 'Age',
        'form.renda_mensal': 'Monthly Income',
        'form.divida_total': 'Total Debt',
        'form.limite_credito': 'Credit Limit',
        'form.saldo_utilizado': 'Used Balance',
        'form.valor_parcela': 'Payment Amount',
        'form.renda_std_6m': 'Income Volatility',
        'form.idade_credito_meses': 'Credit Age (months)',
        'form.tempo_emprego_meses': 'Employment Time (months)',
        'form.atrasos_30d': 'Late 30-59 days',
        'form.atrasos_90d': 'Late 90+ days',
        'form.pagamentos_dia': 'On-Time Payments',
        'form.btn.example': 'Fill example',
        'form.btn.submit': 'Analyze credit',
        
        // Result
        'result.approved': 'Approved',
        'result.rejected': 'Rejected',
        'result.score': 'Risk Score',
        'result.customer': 'Customer',
        'result.category': 'Category',
        'result.limit': 'Recommended Limit',
        'result.timestamp': 'Timestamp',
        'result.risk.low': 'Low',
        'result.risk.medium': 'Medium',
        'result.risk.high': 'High',
        'result.btn.new': 'New analysis',
        
        // Loading & Error
        'loading.text': 'Processing analysis...',
        'error.title': 'Processing error',
        'error.message': 'An error occurred while processing your request.',
        'error.btn': 'Try again',
        
        // Footer
        'footer.description': 'Credit analysis system based on Machine Learning',
        'footer.copyright': '© 2026 Credit Scoring. Developed for educational purposes.'
    }
};

// Initialize i18n
let currentLang = localStorage.getItem('language') || 'pt';

function setLanguage(lang) {
    currentLang = lang;
    localStorage.setItem('language', lang);
    
    // Update all elements with data-i18n attribute
    document.querySelectorAll('[data-i18n]').forEach(element => {
        const key = element.getAttribute('data-i18n');
        if (translations[lang][key]) {
            element.textContent = translations[lang][key];
        }
    });
    
    // Update placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(element => {
        const key = element.getAttribute('data-i18n-placeholder');
        if (translations[lang][key]) {
            element.placeholder = translations[lang][key];
        }
    });
    
    // Update active language button
    document.querySelectorAll('.lang-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.querySelector(`.lang-btn[data-lang="${lang}"]`)?.classList.add('active');
}

// Initialize language on load
document.addEventListener('DOMContentLoaded', function() {
    setLanguage(currentLang);
});

// Dark Mode functionality
let currentTheme = localStorage.getItem('theme') || 'light';

function toggleTheme() {
    currentTheme = currentTheme === 'light' ? 'dark' : 'light';
    applyTheme(currentTheme);
}

function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('theme', theme);
}

// Initialize theme on load
document.addEventListener('DOMContentLoaded', function() {
    applyTheme(currentTheme);
    setLanguage(currentLang);
});