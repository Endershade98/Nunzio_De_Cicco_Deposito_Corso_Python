# =====================================
# 1. Importazione librerie
# =====================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression, LassoCV, Lasso, RidgeCV, Ridge, ElasticNetCV, ElasticNet
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.decomposition import PCA
from sklearn.ensemble import GradientBoostingRegressor

from math import sqrt
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# =====================================
# 2. Caricamento e pre-processing dei dati
# =====================================
df = pd.read_csv('/home/endershade/Desktop/Python_Course_Repo/lesson_23_wed_30_apr/AB_NYC_2019.csv')

df['date'] = df['date'].str.replace('T000000', '', regex=False)
df["date"] = pd.to_datetime(df["date"], format="%Y%m%d")

df['yr_renovated'] = pd.cut(df['yr_renovated'], bins=[-1, 0, 1980, 2000, float('inf')],
                            labels=[0, 1, 2, 3])

# =====================================
# 3. Definizione variabili + scaling
# =====================================
X = df.drop(columns=["price", "date", "id"])
y = df["price"]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
y_scaled = scaler.fit_transform(y.values.reshape(-1, 1))

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

# =====================================
# 4. Funzione per eliminazione VIF e p-value
# =====================================
def elimina_variabili_vif_pvalue(X_train, y_train, vif_threshold=10.0, pvalue_threshold=0.05):
    if not isinstance(X_train, pd.DataFrame):
        X_current = pd.DataFrame(X_train, columns=[f"x{i}" for i in range(X_train.shape[1])])
    else:
        X_current = X_train.copy()

    while True:
        X_const = sm.add_constant(X_current)
        model = sm.OLS(y_train, X_const).fit()

        pvalues = model.pvalues.drop('const')
        vif = pd.DataFrame({
            "Feature": X_current.columns,
            "VIF": [variance_inflation_factor(X_current.values, i) for i in range(X_current.shape[1])]
        })

        stats = vif.copy()
        stats["p-value"] = pvalues.values

        candidates = stats[(stats["VIF"] > vif_threshold) & (stats["p-value"] > pvalue_threshold)]
        if candidates.empty:
            print("\nNessuna variabile da eliminare. Selezione completata.")
            break

        worst = candidates.sort_values(by="VIF", ascending=False).iloc[0]
        feat = worst["Feature"]
        print(f"Rimuovo '{feat}' (VIF={worst['VIF']:.2f}, p-value={worst['p-value']:.4f})")
        X_current = X_current.drop(columns=[feat])

    print("\nFeature finali selezionate:")
    print(X_current.columns.tolist())
    return X_current

# =====================================
# 5. Linear Regression
# =====================================
X_current = elimina_variabili_vif_pvalue(X_train, y_train)

model = LinearRegression()
model.fit(X_current, y_train)
y_pred = model.predict(X_test)

rmse = sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Linear Regression → RMSE: {rmse:.2f}, R²: {r2:.2f}")

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Valori reali")
plt.ylabel("Valori predetti")
plt.title("Confronto tra valori reali e predetti")
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.show()

# =====================================
# 6. Lasso, Ridge, ElasticNet con CV
# =====================================
lasso_cv = LassoCV(alphas=[0.1, 0.5, 1.0, 5.0, 10.0], cv=5, random_state=0)
ridge_cv = RidgeCV(alphas=[0.1, 0.5, 1.0, 5.0, 10.0], cv=5)
elastic_cv = ElasticNetCV(
    alphas=[0.1, 0.5, 1.0, 5.0, 10.0],
    l1_ratio=[0.1, 0.5, 0.7, 0.9, 0.95, 0.99, 1.0],
    cv=5,
    random_state=0
)

lasso_cv.fit(X_current, y_train)
ridge_cv.fit(X_current, y_train)
elastic_cv.fit(X_current, y_train)

print(f"Best alpha per Lasso:      {lasso_cv.alpha_:.4f}")
print(f"Best alpha per Ridge:      {ridge_cv.alpha_:.4f}")
print(f"Best alpha per ElasticNet: {elastic_cv.alpha_:.4f}")
print(f"Best l1_ratio (ElasticNet):{elastic_cv.l1_ratio_:.4f}")

lasso = Lasso(alpha=lasso_cv.alpha_, random_state=0)
ridge = Ridge(alpha=ridge_cv.alpha_)
elastic = ElasticNet(alpha=elastic_cv.alpha_, l1_ratio=elastic_cv.l1_ratio_, random_state=0)

lasso.fit(X_current, y_train)
ridge.fit(X_current, y_train)
elastic.fit(X_current, y_train)

y_pred_lasso = lasso.predict(X_test)
y_pred_ridge = ridge.predict(X_test)
y_pred_elastic = elastic.predict(X_test)

print("\nConfronto modelli su test set:")
print("=" * 40)
print(f"Lasso     → R²: {r2_score(y_test, y_pred_lasso):.4f}, RMSE: {sqrt(mean_squared_error(y_test, y_pred_lasso)):.4f}")
print(f"Ridge     → R²: {r2_score(y_test, y_pred_ridge):.4f}, RMSE: {sqrt(mean_squared_error(y_test, y_pred_ridge)):.4f}")
print(f"ElasticNet→ R²: {r2_score(y_test, y_pred_elastic):.4f}, RMSE: {sqrt(mean_squared_error(y_test, y_pred_elastic)):.4f}")


# =====================================
# 7. PCA e Linear Regression
# =====================================

pca = PCA()
X_train_pca = pca.fit_transform(X_train)

plt.figure(figsize=(10, 6))
plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Explained Variance by Components')
plt.grid(True)
plt.axhline(y=0.95, color='r', linestyle='--', label='95% Explained Variance')
plt.legend()
plt.show()

n_components = np.argmax(np.cumsum(pca.explained_variance_ratio_) >= 0.95) + 1
print(f"Number of components needed for 95% variance: {n_components}")

pca_optimal = PCA(n_components=n_components)
X_train_pca_optimal = pca_optimal.fit_transform(X_train)
X_test_pca_optimal = pca_optimal.transform(X_test)

model_pca = LinearRegression()
model_pca.fit(X_train_pca_optimal, y_train)
y_pred_pca = model_pca.predict(X_test_pca_optimal)

print(f"PCA Model → R²: {r2_score(y_test, y_pred_pca):.4f}, RMSE: {sqrt(mean_squared_error(y_test, y_pred_pca)):.4f}")


# =====================================
# 8. Gradient Boosting e GridSearchCV
# =====================================

# Parametri da testare
param_grid = {
    'n_estimators': [100, 200],
    'learning_rate': [0.05, 0.1],
    'max_depth': [3, 5],
    'subsample': [0.8, 1.0]
}

gbr = GradientBoostingRegressor(random_state=0)
grid_search = GridSearchCV(gbr, param_grid, cv=5, scoring='r2', n_jobs=-1)
grid_search.fit(X_current, y_train)

best_gbr = grid_search.best_estimator_

y_pred_gbr = best_gbr.predict(X_test)

print("\nGradient Boosting Regressor:")
print(f"Best Params: {grid_search.best_params_}")
print(f"R²: {r2_score(y_test, y_pred_gbr):.4f}")
print(f"RMSE: {sqrt(mean_squared_error(y_test, y_pred_gbr)):.4f}")


# =====================================
# 9. Gradient Boosting con GridSearchCV
# =====================================

# Definizione griglia di parametri
param_grid = {
    'n_estimators': [100, 200],
    'learning_rate': [0.05, 0.1],
    'max_depth': [3, 5],
    'subsample': [0.8, 1.0]
}

# Istanziazione e ricerca
gbr_grid = GradientBoostingRegressor(random_state=0)
grid_search = GridSearchCV(estimator=gbr_grid,
                           param_grid=param_grid,
                           cv=5,
                           scoring='r2',
                           n_jobs=-1,
                           verbose=1)

grid_search.fit(X_current, y_train)
best_gbr = grid_search.best_estimator_

# Valutazione
y_pred_gbr_grid = best_gbr.predict(X_test)
r2_gbr_grid = r2_score(y_test, y_pred_gbr_grid)
rmse_gbr_grid = sqrt(mean_squared_error(y_test, y_pred_gbr_grid))

print("\nGradient Boosting (GridSearchCV):")
print(f"Best Params: {grid_search.best_params_}")
print(f"R²:   {r2_gbr_grid:.4f}")
print(f"RMSE: {rmse_gbr_grid:.4f}")
