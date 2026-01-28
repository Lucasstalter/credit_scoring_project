import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

@pytest.fixture
def sample_data():
    np.random.seed(42)
    n_samples = 1000
    
    data = {
        'customer_id': [f'CUST{i:04d}' for i in range(n_samples)],
        'idade': np.random.randint(18, 70, n_samples),
        'renda_mensal': np.random.uniform(1000, 20000, n_samples),
        'divida_total': np.random.uniform(0, 50000, n_samples),
        'limite_credito': np.random.uniform(1000, 30000, n_samples),
        'saldo_utilizado': np.random.uniform(0, 20000, n_samples),
        'valor_parcela': np.random.uniform(100, 2000, n_samples),
        'idade_credito_meses': np.random.randint(0, 120, n_samples),
        'tempo_emprego_meses': np.random.randint(0, 240, n_samples),
        'atrasos_30d': np.random.randint(0, 5, n_samples),
        'atrasos_90d': np.random.randint(0, 3, n_samples),
        'pagamentos_dia': np.random.randint(0, 12, n_samples),
        'renda_std_6m': np.random.uniform(0, 1000, n_samples),
        'default': np.random.binomial(1, 0.2, n_samples)
    }
    
    return pd.DataFrame(data)

@pytest.fixture
def sample_application():
    return {
        "customer_id": "TEST001",
        "idade": 35,
        "renda_mensal": 5000.0,
        "divida_total": 15000.0,
        "limite_credito": 10000.0,
        "saldo_utilizado": 7000.0,
        "valor_parcela": 500.0,
        "idade_credito_meses": 60,
        "tempo_emprego_meses": 24,
        "atrasos_30d": 1,
        "atrasos_90d": 0,
        "pagamentos_dia": 11,
        "renda_std_6m": 200.0
    }
