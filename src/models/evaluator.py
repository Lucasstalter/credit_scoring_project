from sklearn.metrics import roc_auc_score, confusion_matrix
import pandas as pd

class ModelEvaluator:
    def __init__(self, model, X_test, y_test):
        self.model = model
        self.X_test = X_test
        self.y_test = y_test
        self.y_pred_proba = model.predict_proba(X_test)
        self.metrics = {}
    
    def calculate_metrics(self, threshold=0.5):
        y_pred = (self.y_pred_proba >= threshold).astype(int)
        
        self.metrics['auc_roc'] = roc_auc_score(self.y_test, self.y_pred_proba)
        cm = confusion_matrix(self.y_test, y_pred)
        tn, fp, fn, tp = cm.ravel()
        
        self.metrics['accuracy'] = (tp + tn) / (tp + tn + fp + fn)
        self.metrics['precision'] = tp / (tp + fp) if (tp + fp) > 0 else 0
        self.metrics['recall'] = tp / (tp + fn) if (tp + fn) > 0 else 0
        
        return self.metrics
