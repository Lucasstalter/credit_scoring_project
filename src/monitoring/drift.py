import pandas as pd

class DriftMonitor:
    def __init__(self, reference_data: pd.DataFrame, threshold: float = 0.05):
        self.reference_data = reference_data
        self.threshold = threshold
    
    def detect_drift(self, current_data: pd.DataFrame):
        return {
            'drift_detected': False,
            'drifted_features': [],
            'num_drifted': 0
        }
