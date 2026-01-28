import xgboost as xgb
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
import numpy as np

class CreditScoringModel:
    def __init__(self, config):
        self.config = config
        self.model = None
        self.feature_names = None
    
    def train(self, X_train, y_train):
        self.feature_names = X_train.columns.tolist()
        dtrain = xgb.DMatrix(X_train, label=y_train)
        
        params = {
            'objective': 'binary:logistic',
            'eval_metric': 'auc',
            'max_depth': 6,
            'learning_rate': 0.05
        }
        
        self.model = xgb.train(params, dtrain, num_boost_round=100)
        return self
    
    def predict_proba(self, X):
        dtest = xgb.DMatrix(X)
        return self.model.predict(dtest)
    
    def predict(self, X, threshold=0.5):
        return (self.predict_proba(X) >= threshold).astype(int)
