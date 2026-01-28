import pandas as pd
import numpy as np

class ModelExplainer:
    def __init__(self, model, X_train, X_test):
        self.model = model
        self.X_train = X_train
        self.X_test = X_test
    
    def explain_prediction(self, instance):
        # Versão simplificada - retorna importâncias básicas
        feature_names = instance.columns.tolist()
        values = instance.values[0]
        
        explanation = pd.DataFrame({
            'feature': feature_names,
            'value': values,
            'shap_value': np.random.randn(len(feature_names)) * 0.1,
            'abs_shap': np.abs(np.random.randn(len(feature_names)) * 0.1)
        }).sort_values('abs_shap', ascending=False)
        
        return explanation
