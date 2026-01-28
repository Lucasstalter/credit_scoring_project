"""
Treinamento com Dataset Real - Give Me Some Credit
"""
import pandas as pd
import numpy as np
import joblib
from pathlib import Path
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, classification_report, confusion_matrix
import xgboost as xgb

print("="*70)
print("TREINAMENTO COM DATASET REAL - GIVE ME SOME CREDIT")
print("="*70)

# 1. CARREGAR DADOS
print("\n[1/8] Carregando dataset real...")
data_path = Path('data/raw/cs-training.csv')

if not data_path.exists():
    print(f"\n✗ Arquivo não encontrado: {data_path}")
    print("\nBaixe o dataset em:")
    print("https://www.kaggle.com/c/GiveMeSomeCredit/data")
    exit(1)

df = pd.read_csv(data_path)
print(f"✓ {len(df):,} amostras carregadas")
print(f"  Colunas: {len(df.columns)}")
print(f"  Taxa de default: {df['SeriousDlqin2yrs'].mean():.2%}")

# 2. ANÁLISE INICIAL
print("\n[2/8] Analisando dados...")
print(f"\nMissing values:")
missing = df.isnull().sum()
for col in missing[missing > 0].index:
    pct = (missing[col] / len(df)) * 100
    print(f"  {col}: {missing[col]:,} ({pct:.1f}%)")

# 3. LIMPEZA E PREPARAÇÃO
print("\n[3/8] Limpando dados...")

# Remover coluna de índice se existir
if 'Unnamed: 0' in df.columns:
    df = df.drop('Unnamed: 0', axis=1)

# Target
y = df['SeriousDlqin2yrs']
X = df.drop('SeriousDlqin2yrs', axis=1)

# Tratar missing values
print("  Tratando missing values...")
if X['MonthlyIncome'].isnull().any():
    X['MonthlyIncome'].fillna(X['MonthlyIncome'].median(), inplace=True)

if X['NumberOfDependents'].isnull().any():
    X['NumberOfDependents'].fillna(0, inplace=True)

# Tratar outliers
print("  Tratando outliers...")
X['age'] = X['age'].clip(18, 100)
X['RevolvingUtilizationOfUnsecuredLines'] = X['RevolvingUtilizationOfUnsecuredLines'].clip(0, 2)
X['DebtRatio'] = X['DebtRatio'].clip(0, 10)

print(f"✓ Dados limpos: {X.shape}")

# 4. FEATURE ENGINEERING
print("\n[4/8] Feature Engineering...")

X['high_utilization'] = (X['RevolvingUtilizationOfUnsecuredLines'] > 0.8).astype(int)
X['has_late_payment'] = ((X['NumberOfTime30-59DaysPastDueNotWorse'] > 0) | 
                          (X['NumberOfTime60-89DaysPastDueNotWorse'] > 0) |
                          (X['NumberOfTimes90DaysLate'] > 0)).astype(int)
X['total_late_payments'] = (X['NumberOfTime30-59DaysPastDueNotWorse'] + 
                             X['NumberOfTime60-89DaysPastDueNotWorse'] +
                             X['NumberOfTimes90DaysLate'])
X['age_group'] = pd.cut(X['age'], bins=[0, 25, 35, 50, 65, 100], labels=[1,2,3,4,5]).astype(int)
X['income_debt_ratio'] = X['MonthlyIncome'] / (X['DebtRatio'] + 1)

print(f"✓ {X.shape[1]} features totais")

# 5. SPLIT TRAIN/TEST
print("\n[5/8] Dividindo dados...")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)
print(f"✓ Train: {len(X_train):,} | Test: {len(X_test):,}")
print(f"  Default rate train: {y_train.mean():.2%}")
print(f"  Default rate test: {y_test.mean():.2%}")

# 6. TREINAR MODELO OTIMIZADO
print("\n[6/8] Treinando XGBoost otimizado...")

scale_pos_weight = (y_train == 0).sum() / (y_train == 1).sum()
print(f"  Scale pos weight: {scale_pos_weight:.2f}")

params = {
    'objective': 'binary:logistic',
    'eval_metric': 'auc',
    'scale_pos_weight': scale_pos_weight,
    'max_depth': 6,
    'learning_rate': 0.05,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'min_child_weight': 3,
    'gamma': 0.1,
    'reg_alpha': 0.1,
    'reg_lambda': 1
}

dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

evals = [(dtrain, 'train'), (dtest, 'test')]

model = xgb.train(
    params,
    dtrain,
    num_boost_round=500,
    evals=evals,
    early_stopping_rounds=50,
    verbose_eval=50
)

print(f"✓ Modelo treinado! Best iteration: {model.best_iteration}")

# 7. AVALIAR
print("\n[7/8] Avaliando modelo...")

y_pred_proba = model.predict(dtest)
y_pred = (y_pred_proba >= 0.5).astype(int)

auc = roc_auc_score(y_test, y_pred_proba)

cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

precision = tp / (tp + fp) if (tp + fp) > 0 else 0
recall = tp / (tp + fn) if (tp + fn) > 0 else 0
f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

metrics = {
    'auc_roc': auc,
    'precision': precision,
    'recall': recall,
    'f1_score': f1,
    'true_negatives': int(tn),
    'false_positives': int(fp),
    'false_negatives': int(fn),
    'true_positives': int(tp)
}

print("\n" + "="*70)
print("MÉTRICAS DO MODELO - DATASET REAL")
print("="*70)
print(f"AUC-ROC:   {auc:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-Score:  {f1:.4f}")
print("\nConfusion Matrix:")
print(f"  True Negatives:  {tn:,}")
print(f"  False Positives: {fp:,}")
print(f"  False Negatives: {fn:,}")
print(f"  True Positives:  {tp:,}")
print("="*70)

# Feature Importance
print("\nTop 10 Features mais importantes:")
importance = model.get_score(importance_type='weight')
importance_sorted = sorted(importance.items(), key=lambda x: x[1], reverse=True)[:10]
for feat, score in importance_sorted:
    print(f"  {feat}: {score}")

# 8. SALVAR MODELO
print("\n[8/8] Salvando modelo...")
model_dir = Path('models/production')
model_dir.mkdir(parents=True, exist_ok=True)

artifacts = {
    'model': model,
    'feature_names': X_train.columns.tolist(),
    'params': params,
    'metrics': metrics,
    'version': datetime.now().strftime('%Y%m%d_%H%M%S'),
    'dataset': 'GiveMeSomeCredit',
    'n_samples': len(df)
}

model_path = model_dir / 'model_latest.pkl'
joblib.dump(artifacts, model_path)
print(f"✓ Modelo salvo: {model_path}")

timestamp_path = model_dir / f'model_real_{artifacts["version"]}.pkl'
joblib.dump(artifacts, timestamp_path)
print(f"✓ Backup salvo: {timestamp_path}")

# 9. TESTE DE PREDIÇÃO
print("\n" + "="*70)
print("TESTANDO PREDIÇÃO")
print("="*70)

sample_idx = X_test.index[0]
sample = X_test.loc[[sample_idx]]
sample_proba = model.predict(xgb.DMatrix(sample))[0]

print(f"Cliente de teste:")
print(f"  Idade: {int(sample['age'].values[0])}")
print(f"  Renda Mensal: ${sample['MonthlyIncome'].values[0]:,.0f}")
print(f"  Debt Ratio: {sample['DebtRatio'].values[0]:.2f}")
print(f"  Atrasos 90d: {int(sample['NumberOfTimes90DaysLate'].values[0])}")
print(f"\nScore previsto: {sample_proba:.4f}")
print(f"Decisão: {'APROVADO' if sample_proba < 0.5 else 'NEGADO'}")
print(f"Real: {'INADIMPLENTE' if y_test.loc[sample_idx] == 1 else 'ADIMPLENTE'}")

print("\n" + "="*70)
print("TREINAMENTO COMPLETO COM DADOS REAIS! ✓")
print("="*70)
print(f"\nReinicie a API para usar o novo modelo:")
print(f"  docker-compose restart api")