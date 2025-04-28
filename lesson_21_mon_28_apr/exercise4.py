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
from sklearn.tree import DecisionTreeClassifier

# Carica il dataset Wine
wine = datasets.load_wine()  # Carica il dataset Wine da sklearn
X = wine.data  # Estrai le feature
y = wine.target  # Estrai i target
feature_names = wine.feature_names  # I nomi delle feature
target_names = wine.target_names  # I nomi delle classi target

# Esplora il dataset
# Visualizza il numero di campioni per ciascuna classe
print("Numero di campioni per ciascuna classe:")
print(pd.Series(y).value_counts())  # Conta il numero di campioni per ogni classe

# Calcola le statistiche di base delle feature
print("\nStatistiche di base delle feature:")
df = pd.DataFrame(X, columns=feature_names)  # Crea un DataFrame con le feature
print(df.describe())  # Stampa le statistiche descrittive

# Visualizzazione: crea un grafico a barre per mostrare la distribuzione delle classi
plt.figure(figsize=(6,4))
sns.countplot(x=y)
plt.title('Distribuzione delle classi nel dataset Wine')
plt.xlabel('Classe')
plt.ylabel('Numero di campioni')
plt.show()

# Riduci la dimensionalità (PCA)
pca = PCA(n_components=2)  # Imposta PCA per ridurre le dimensioni a 2 componenti principali
X_pca = pca.fit_transform(X)  # Applica PCA ai dati

# Visualizzazione dei dati trasformati con PCA in un grafico scatter 2D
plt.figure(figsize=(8,6))
scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis', edgecolor='k', s=50)
legend1 = plt.legend(*scatter.legend_elements(), title="Classi")  # Legenda automatica
plt.gca().add_artist(legend1)  # Aggiungi la legenda al grafico
plt.title('PCA - Riduzione a 2 componenti')
plt.xlabel('PC 1')
plt.ylabel('PC 2')
plt.show()

# Suddividi i dati in training e test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Applica un algoritmo di classificazione (RandomForest)
clf = RandomForestClassifier(random_state=42)  # Crea un modello Random Forest
clf.fit(X_train, y_train)  # Allena il modello con i dati di training

# Valuta la performance del modello
y_pred = clf.predict(X_test)  # Predici i valori sui dati di test

# Stampa le metriche di valutazione del modello
print("\nValutazione del modello:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Precision: {precision_score(y_test, y_pred, average='weighted'):.2f}")
print(f"Recall: {recall_score(y_test, y_pred, average='weighted'):.2f}")
print(f"F1 Score: {f1_score(y_test, y_pred, average='weighted'):.2f}")

print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=target_names))

# Visualizza l'importanza delle feature
importances = clf.feature_importances_  # Estrai l'importanza delle feature
indices = np.argsort(importances)[::-1]  # Ordina le feature in base all'importanza

plt.figure(figsize=(10,6))
sns.barplot(x=importances[indices], y=np.array(feature_names)[indices])
plt.title('Importanza delle feature (Random Forest)')
plt.show()

# Visualizza la matrice di confusione
cm = confusion_matrix(y_test, y_pred)  # Calcola la matrice di confusione

plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=target_names, yticklabels=target_names)
plt.title('Matrice di Confusione')
plt.xlabel('Predetto')
plt.ylabel('Reale')
plt.show()

# Ottimizza l'algoritmo (GridSearchCV)
param_grid = {  # Parametri da ottimizzare tramite GridSearchCV
    'n_estimators': [50, 100, 150],  # Numero di alberi
    'max_depth': [None, 5, 10, 20]    # Profondità massima degli alberi
}

grid_search = GridSearchCV(RandomForestClassifier(random_state=42), param_grid, cv=5, scoring='accuracy')  # Grid search per ottimizzare i parametri
grid_search.fit(X_train, y_train)  # Addestra GridSearchCV sui dati di training

# Stampa i migliori parametri trovati
print("\nMigliori parametri trovati da GridSearchCV:")
print(grid_search.best_params_)

# Valutazione finale con modello ottimizzato
best_model = grid_search.best_estimator_  # Estrai il modello migliore
y_pred_best = best_model.predict(X_test)  # Predici con il modello ottimizzato

# Stampa le metriche di valutazione per il modello ottimizzato
print("\nValutazione finale con modello ottimizzato:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_best):.2f}")
print(f"Precision: {precision_score(y_test, y_pred_best, average='weighted'):.2f}")
print(f"Recall: {recall_score(y_test, y_pred_best, average='weighted'):.2f}")
print(f"F1 Score: {f1_score(y_test, y_pred_best, average='weighted'):.2f}")
