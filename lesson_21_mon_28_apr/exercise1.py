import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (accuracy_score, precision_score, recall_score,
                             f1_score, confusion_matrix, classification_report)
from sklearn.tree import DecisionTreeClassifier  # <- Import corretto
from sklearn.model_selection import StratifiedKFold

# Carica il dataset Wine
wine = datasets.load_wine()
X = wine.data
y = wine.target
feature_names = wine.feature_names
target_names = wine.target_names

# Esplora il dataset
print("Numero di campioni per ciascuna classe:")
print(pd.Series(y).value_counts())

print("\nStatistiche di base delle feature:")
df = pd.DataFrame(X, columns=feature_names)
print(df.describe())

# Visualizzazione: distribuzione delle classi
plt.figure(figsize=(6,4))
sns.countplot(x=y)
plt.title('Distribuzione delle classi nel dataset Wine')
plt.xlabel('Classe')
plt.ylabel('Numero di campioni')
plt.show()

# Riduci la dimensionalità (PCA)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# Visualizzazione PCA
plt.figure(figsize=(8,6))
scatter = plt.scatter(X_pca[:,0], X_pca[:,1], c=y, cmap='viridis', edgecolor='k', s=50)
legend1 = plt.legend(*scatter.legend_elements(), title="Classi")
plt.gca().add_artist(legend1)
plt.title('PCA - Riduzione a 2 componenti')
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.show()

# Suddividi i dati in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Applica un algoritmo di classificazione (RandomForest)
clf = RandomForestClassifier(random_state=42)
clf.fit(X_train, y_train)

# Valuta la performance del modello
y_pred = clf.predict(X_test)

print("\nValutazione del modello:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.2f}")
print(f"Recall: {recall_score(y_test, y_pred, average='weighted'):.2f}")
print(f"F1 Score: {f1_score(y_test, y_pred, average='weighted'):.2f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Visualizza l'importanza delle feature
importances = clf.feature_importances_
indices = np.argsort(importances)[::-1]

plt.figure(figsize=(10,6))
sns.barplot(x=importances[indices], y=np.array(feature_names)[indices])
plt.title('Importanza delle feature (Random Forest)')
plt.show()

# Visualizza la matrice di confusione
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=target_names, yticklabels=target_names)
plt.title('Matrice di Confusione')
plt.xlabel('Predetto')
plt.ylabel('Reale')
plt.show()

# Ottimizza Random Forest (GridSearchCV)
param_grid_rf = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 5, 10, 20]
}

grid_search_rf = GridSearchCV(RandomForestClassifier(random_state=42), param_grid_rf, cv=5, scoring='accuracy')
grid_search_rf.fit(X_train, y_train)

print("\nMigliori parametri trovati da GridSearchCV (Random Forest):")
print(grid_search_rf.best_params_)

# Valutazione finale con modello ottimizzato
best_model = grid_search_rf.best_estimator_
y_pred_best = best_model.predict(X_test)

print("\nValutazione finale con modello ottimizzato:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_best):.2f}")
print(f"Precision: {precision_score(y_test, y_pred_best, average='weighted'):.2f}")
print(f"Recall: {recall_score(y_test, y_pred_best, average='weighted'):.2f}")
print(f"F1 Score: {f1_score(y_test, y_pred_best, average='weighted'):.2f}")

# Ottimizza Decision Tree (GridSearchCV)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
param_grid_dt = {'max_depth': [3, 5, 7], 'criterion': ['gini', 'entropy']}
grid_search_dt = GridSearchCV(DecisionTreeClassifier(), param_grid_dt, cv=cv)
grid_search_dt.fit(X_train, y_train)

print(f"\nMigliori parametri (Decision Tree): {grid_search_dt.best_params_}")