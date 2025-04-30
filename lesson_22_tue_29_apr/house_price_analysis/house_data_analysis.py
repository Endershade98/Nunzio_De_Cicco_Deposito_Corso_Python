# house_price_analysis.py
# 1. Caricamento e ispezione iniziale del dataset
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant


# Caricamento dataset
df = pd.read_csv('/home/endershade/Desktop/Python_Course_Repo/lesson_22_tue_29_apr/house_price_analysis/kc_house_data.csv')  # Sostituire con il path corretto
print(df.head())
print(df.info())
print(df.describe())

# 2. Pulizia dei dati
# Rimozione colonne non rilevanti
df.drop(columns=['id', 'date'], inplace=True)

# Verifica valori nulli
df = df.dropna()

# Rimozione outlier esempio: bedrooms > 10
df = df[df['bedrooms'] <= 10]

# 3. Analisi delle correlazioni
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(16, 12))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title('Matrice di Correlazione')
plt.show()

# 4. Separazione delle variabili predittive e target
X = df.drop(columns=['price'])
y = df['price']

# 5. Random Forest: Importanza delle feature
rf = RandomForestRegressor(random_state=42)
rf.fit(X, y)

importances = pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False)
print("Importanza delle feature (Random Forest):")
print(importances)

# Visualizzazione importanza
importances.plot(kind='bar', figsize=(12, 6))
plt.title("Importanza delle Feature (Random Forest)")
plt.show()

# 6. Decision Tree: Addestramento e valutazione
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
dt = DecisionTreeRegressor(random_state=42)
dt.fit(X_train, y_train)

y_pred = dt.predict(X_test)
print("R^2 Score (Decision Tree):", r2_score(y_test, y_pred))
print("MSE (Decision Tree):", mean_squared_error(y_test, y_pred))

# 7. Grid Search: Ottimizzazione dei parametri per Decision Tree
param_grid = {
    'max_depth': [5, 10, 15, None],
    'min_samples_split': [2, 10, 20],
    'min_samples_leaf': [1, 5, 10]
}

grid_search = GridSearchCV(DecisionTreeRegressor(random_state=42), param_grid, cv=5, scoring='r2')
grid_search.fit(X_train, y_train)
print("Migliori parametri trovati:", grid_search.best_params_)

# 8. Valutazione del miglior modello ottenuto
best_model = grid_search.best_estimator_
y_best_pred = best_model.predict(X_test)
print("R^2 (modello ottimizzato):", r2_score(y_test, y_best_pred))
print("MSE:", mean_squared_error(y_test, y_best_pred))

# 9. Inizializza e allena il modello (Linear Regression)
lr = LinearRegression()
lr.fit(X_train, y_train)

# 10. Calcolo dell'R^2 per la Linear Regression
y_lr_pred = lr.predict(X_test)
print("R^2 (Linear Regression):", r2_score(y_test, y_lr_pred))

# 11. Grafico Boxplot su tutte le feature
plt.figure(figsize=(20, 10))
df.boxplot(rot=90)
plt.title('Boxplot di tutte le Feature')
plt.xticks(rotation=45)
plt.show()
