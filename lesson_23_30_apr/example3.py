import xgboost as xgb
from sklearn.datasets import load_diabetes
import numpy as np

# Carica il dataset (es. diabetes)
diabetes = load_diabetes()
X, y = diabetes.data, diabetes.target

# Crea il DMatrix
dtrain = xgb.DMatrix(X, label=y, missing=np.nan)

# Parametri iniziali
params = {
    'objective': 'reg:squarederror',
    'eta': 0.1,
    'max_depth': 4,
}

# Definizione della griglia per alpha e lambda
param_grid = {
    'alpha': [0, 0.1, 0.5, 1],
    'lambda': [0, 0.1, 0.5, 1]
}

best_params = {}
best_rmse = float("inf")

# Ricerca a griglia
for alpha in param_grid['alpha']:
    for lam in param_grid['lambda']:  # evitiamo di sovrascrivere "lambda", che è una parola chiave in Python
        params['alpha'] = alpha
        params['lambda'] = lam
        cv_results = xgb.cv(
            params,
            dtrain,
            num_boost_round=100,
            nfold=5,
            metrics="rmse",
            early_stopping_rounds=10,
            seed=42,
            verbose_eval=False
        )
        mean_rmse = cv_results['test-rmse-mean'].min()
        print(f"alpha: {alpha}, lambda: {lam}, RMSE: {mean_rmse:.4f}")
        if mean_rmse < best_rmse:
            best_rmse = mean_rmse
            best_params = {'alpha': alpha, 'lambda': lam}

print(f"\nMigliori parametri: {best_params} con RMSE: {best_rmse:.4f}")
