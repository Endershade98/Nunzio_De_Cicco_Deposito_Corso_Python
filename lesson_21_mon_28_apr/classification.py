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


class WineClassifier:
    """Rappresenta un Classificatore per la classe Wine"""
    def __init__(self, random_state=42):
        """Carica il dataset Wine"""
        wine = datasets.load_wine() # carica il dataset
        self.X = wine.data
        self.y = wine.target
        self.feature_names = wine.feature_names
        self.target_names = wine.target_names
        self.random_state = random_state # default 42
        self.clf = RandomForestClassifier(random_state=random_state) # classificatore usato
        self.model_trained = False # status del modello
        self.pca_applied = False # status della pca
    
    def explore_data(self):
        # Esplora il dataset
        print("Numero di campioni per ciascuna classe:")
        print(pd.Series(self.y).value_counts())  # Conta il numero di campioni per ogni classe
        print("\nStatistiche di base delle feature:")
        df = pd.DataFrame(self.X, columns=self.feature_names)  # Crea un DataFrame con le feature
        print(df.describe())  # Stampa le statistiche descrittive

        # Visualizzazione: crea un grafico a barre per mostrare la distribuzione delle classi
        plt.figure(figsize=(6, 4))
        sns.countplot(x=self.y)
        plt.title('Distribuzione delle classi nel dataset Wine')
        plt.xlabel('Classe')
        plt.ylabel('Numero di campioni')
        plt.show()
    
    def reduce_dimensionality(self):
        # Riduci la dimensionalità (PCA)
        pca = PCA(n_components=2)  # Imposta PCA per ridurre le dimensioni a 2 componenti principali
        self.X_pca = pca.fit_transform(self.X)  # Applica PCA ai dati
        self.pca_applied = True  # Controllo per PCA applicata

        # Visualizzazione dei dati trasformati con PCA in un grafico scatter 2D
        plt.figure(figsize=(8, 6))
        scatter = plt.scatter(self.X_pca[:, 0], self.X_pca[:, 1], c=self.y, cmap='viridis', edgecolor='k', s=50)
        legend1 = plt.legend(*scatter.legend_elements(), title="Classi")  # Legenda automatica
        plt.gca().add_artist(legend1)  # Aggiungi la legenda al grafico
        plt.title('PCA - Riduzione a 2 componenti')
        plt.xlabel('PC 1')
        plt.ylabel('PC 2')
        plt.show()
    
    def train_model(self):
        # Suddividi i dati in training e test set
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=self.random_state, stratify=self.y)
        
        # Addestra il modello RandomForest
        self.clf.fit(self.X_train, self.y_train)
        self.model_trained = True  # Controllo per il modello addestrato
    
    def evaluate_model(self):
        if not self.model_trained:
            print("Errore: Il modello non è stato addestrato. Devi prima allenarlo con 'train_model()'.")
            return
        
        # Valuta la performance del modello
        y_pred = self.clf.predict(self.X_test)

        print("\nValutazione del modello:")
        print(f"Accuracy: {accuracy_score(self.y_test, y_pred):.2f}")
        print(f"Precision: {precision_score(self.y_test, y_pred, average='weighted'):.2f}")
        print(f"Recall: {recall_score(self.y_test, y_pred, average='weighted'):.2f}")
        print(f"F1 Score: {f1_score(self.y_test, y_pred, average='weighted'):.2f}")

        print("\nClassification Report:")
        print(classification_report(self.y_test, y_pred, target_names=self.target_names))
    
    def feature_importance(self):
        if not self.model_trained:
            print("Errore: Il modello non è stato addestrato. Devi prima allenarlo con 'train_model()'.")
            return
        
        # Visualizza l'importanza delle feature
        importances = self.clf.feature_importances_  # Estrai l'importanza delle feature
        indices = np.argsort(importances)[::-1]  # Ordina le feature in base all'importanza

        plt.figure(figsize=(10, 6))
        sns.barplot(x=importances[indices], y=np.array(self.feature_names)[indices])
        plt.title('Importanza delle feature (Random Forest)')
        plt.show()
    
    def confusion_matrix(self):
        if not self.model_trained:
            print("Errore: Il modello non è stato addestrato. Devi prima allenarlo con 'train_model()'.")
            return
        
        # Visualizza la matrice di confusione
        y_pred = self.clf.predict(self.X_test)
        cm = confusion_matrix(self.y_test, y_pred)

        plt.figure(figsize=(6, 5))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=self.target_names, yticklabels=self.target_names)
        plt.title('Matrice di Confusione')
        plt.xlabel('Predetto')
        plt.ylabel('Reale')
        plt.show()
    
    def optimize_model(self):
        if not self.model_trained:
            print("Errore: Il modello non è stato addestrato. Devi prima allenarlo con 'train_model()'.")
            return
        
        # Ottimizza l'algoritmo con GridSearchCV
        param_grid = {  # Parametri da ottimizzare tramite GridSearchCV
            'n_estimators': [50, 100, 150],  # Numero di alberi
            'max_depth': [None, 5, 10, 20]    # Profondità massima degli alberi
        }

        grid_search = GridSearchCV(RandomForestClassifier(random_state=self.random_state), param_grid, cv=5, scoring='accuracy')
        grid_search.fit(self.X_train, self.y_train)  # Addestra GridSearchCV sui dati di training

        # Stampa i migliori parametri trovati
        print("\nMigliori parametri trovati da GridSearchCV:")
        print(grid_search.best_params_)

        # Valutazione finale con modello ottimizzato
        best_model = grid_search.best_estimator_  # Estrai il modello migliore
        y_pred_best = best_model.predict(self.X_test)  # Predici con il modello ottimizzato

        print("\nValutazione finale con modello ottimizzato:")
        print(f"Accuracy: {accuracy_score(self.y_test, y_pred_best):.2f}")
        print(f"Precision: {precision_score(self.y_test, y_pred_best, average='weighted'):.2f}")
        print(f"Recall: {recall_score(self.y_test, y_pred_best, average='weighted'):.2f}")
        print(f"F1 Score: {f1_score(self.y_test, y_pred_best, average='weighted'):.2f}")


