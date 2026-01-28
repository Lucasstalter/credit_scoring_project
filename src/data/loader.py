import pandas as pd
from pathlib import Path
from typing import Tuple

class DataLoader:
    def __init__(self, data_path: str):
        self.data_path = Path(data_path)
    
    def load_raw_data(self) -> pd.DataFrame:
        df = pd.read_csv(self.data_path)
        return df
    
    def validate_schema(self, df: pd.DataFrame) -> bool:
        """Validação básica do schema"""
        required_cols = ['customer_id', 'default']
        
        for col in required_cols:
            if col not in df.columns:
                return False
        
        # Verificar se customer_id é único
        if df['customer_id'].duplicated().any():
            return False
        
        # Verificar se default é 0 ou 1
        if not df['default'].isin([0, 1]).all():
            return False
        
        return True
    
    def split_data(self, df: pd.DataFrame, test_size: float, random_state: int) -> Tuple:
        from sklearn.model_selection import train_test_split
        
        X = df.drop(['customer_id', 'default'], axis=1)
        y = df['default']
        
        return train_test_split(X, y, test_size=test_size, 
                              random_state=random_state, stratify=y)
