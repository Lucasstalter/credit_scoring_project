import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, RobustScaler
from sklearn.impute import SimpleImputer, KNNImputer

class DataPreprocessor:
    def __init__(self):
        self.numeric_imputer = KNNImputer(n_neighbors=5)
        self.categorical_imputer = SimpleImputer(strategy='most_frequent')
        self.scaler = RobustScaler()
        
        self.numeric_features = []
        self.categorical_features = []
    
    def fit(self, X: pd.DataFrame):
        self.numeric_features = X.select_dtypes(include=[np.number]).columns.tolist()
        self.categorical_features = X.select_dtypes(include=['object']).columns.tolist()
        
        if self.numeric_features:
            self.numeric_imputer.fit(X[self.numeric_features])
            self.scaler.fit(X[self.numeric_features])
        
        if self.categorical_features:
            self.categorical_imputer.fit(X[self.categorical_features])
        
        return self
    
    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        X_copy = X.copy()
        
        if self.numeric_features:
            X_copy[self.numeric_features] = self.numeric_imputer.transform(X_copy[self.numeric_features])
            X_copy[self.numeric_features] = self.scaler.transform(X_copy[self.numeric_features])
        
        if self.categorical_features:
            X_copy[self.categorical_features] = self.categorical_imputer.transform(X_copy[self.categorical_features])
            X_copy = pd.get_dummies(X_copy, columns=self.categorical_features, drop_first=True)
        
        return X_copy
    
    def fit_transform(self, X: pd.DataFrame) -> pd.DataFrame:
        return self.fit(X).transform(X)
