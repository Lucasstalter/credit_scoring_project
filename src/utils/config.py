from dataclasses import dataclass
from typing import Dict, List
import yaml

@dataclass
class ModelConfig:
    target_column: str = 'default'
    test_size: float = 0.2
    random_state: int = 42
    cv_folds: int = 5
    
    xgboost_params: Dict = None
    monotonic_constraints: Dict = None
    
    shap_sample_size: int = 1000
    drift_threshold: float = 0.05
    
    def __post_init__(self):
        if self.xgboost_params is None:
            self.xgboost_params = {
                'objective': 'binary:logistic',
                'eval_metric': 'auc',
                'tree_method': 'hist',
                'max_depth': 6,
                'learning_rate': 0.05,
                'subsample': 0.8,
                'colsample_bytree': 0.8,
            }
        
        if self.monotonic_constraints is None:
            self.monotonic_constraints = {
                'idade': 1,
                'renda': -1,
                'divida_renda_ratio': 1,
                'historico_pagamento': -1,
                'tempo_emprego': -1,
            }
    
    @classmethod
    def from_yaml(cls, path: str):
        with open(path, 'r') as f:
            config = yaml.safe_load(f)
        return cls(**config)
