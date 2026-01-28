import pandas as pd
import numpy as np
from typing import List

class FeatureEngineer:
    def __init__(self):
        self.feature_names = []
    
    def create_financial_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        df['divida_renda_ratio'] = df['divida_total'] / (df['renda_mensal'] + 1)
        df['utilizacao_credito'] = df['saldo_utilizado'] / (df['limite_credito'] + 1)
        df['parcela_renda_ratio'] = df['valor_parcela'] / (df['renda_mensal'] + 1)
        
        df['capacidade_pagamento'] = df['renda_mensal'] - df['divida_total']
        df['credito_disponivel'] = df['limite_credito'] - df['saldo_utilizado']
        
        df['idade_credito_anos'] = df['idade_credito_meses'] / 12
        df['tempo_emprego_anos'] = df['tempo_emprego_meses'] / 12
        
        return df
    
    def create_behavioral_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        df['atraso_recente'] = (df['atrasos_30d'] > 0).astype(int)
        df['inadimplencia_grave'] = (df['atrasos_90d'] > 0).astype(int)
        
        df['score_pagamento'] = (
            df['pagamentos_dia'] * 2 - 
            df['atrasos_30d'] * 1 - 
            df['atrasos_90d'] * 3
        )
        
        df['volatilidade_renda'] = df['renda_std_6m'] / (df['renda_mensal'] + 1)
        
        return df
    
    def create_interaction_features(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        
        df['renda_x_idade'] = df['renda_mensal'] * df['idade']
        df['divida_x_inadimplencia'] = df['divida_total'] * df['inadimplencia_grave']
        df['credito_x_utilizacao'] = df['limite_credito'] * df['utilizacao_credito']
        
        return df
    
    def fit_transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = self.create_financial_features(df)
        df = self.create_behavioral_features(df)
        df = self.create_interaction_features(df)
        
        self.feature_names = df.columns.tolist()
        return df
