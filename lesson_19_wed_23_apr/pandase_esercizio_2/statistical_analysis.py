import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve



class ChurnPrediction:
    def __init__(self, file_path):
        # Carica i dati
        self.df = pd.read_csv(file_path)
    
    def show_df_info(self):
        """Mostra informazioni generali sul dataset"""
        print("\nInfo dataset:")
        print(self.df.info())

    def show_stat(self):
        """Mostra statistiche descrittive"""
        print("\nStatistiche descrittive:")
        print(self.df.describe())
    
    def show_churn_distribution(self):
        """Distribuzione della colonna 'Churn'"""
        print("\nDistribuzione 'Churn':")
        print(self.df['Churn'].value_counts())
    
    def clean_data(self):
        """Pre-elaborazione dei dati: rimuovere duplicati, NaN, e correzioni varie"""
        # Rimozione duplicati
        self.df.drop_duplicates(inplace=True)
        
        # Rimozione NaN per le colonne numeriche
        colonne_numeriche = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 
                             'Dati_Consumati', 'Servizio_Clienti_Contatti']
        for col in colonne_numeriche:
            self.df[col].fillna(self.df[col].median(), inplace=True)
        
        # Correzione per età e tariffa mensile
        self.df = self.df[(self.df['Età'] >= 0) & (self.df['Età'] <= 100)]
        self.df = self.df[(self.df['Tariffa_Mensile'] >= 5) & (self.df['Tariffa_Mensile'] <= 200)]
        self.df = self.df[self.df['Dati_Consumati'] >= 0]
        self.df = self.df[self.df['Servizio_Clienti_Contatti'] >= 0]
        
    def feature_engineering(self):
        """Creazione di nuove feature, come 'Costo_per_GB'"""
        self.df['Costo_per_GB'] = self.df.apply(lambda row: row['Tariffa_Mensile'] / row['Dati_Consumati'] if row['Dati_Consumati'] > 0 else 0, axis=1)
    
    def prepare_data(self):
        """Preparazione dei dati per il modello"""
        # Seleziona le colonne numeriche
        colonne_numeriche = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 
                             'Dati_Consumati', 'Servizio_Clienti_Contatti', 'Costo_per_GB']
        X = self.df[colonne_numeriche]
        
        # Converte Churn in formato numerico
        self.df['Churn'] = self.df['Churn'].map({'No': 0, 'Sì': 1})
        y = self.df['Churn']
        
        # Divisione in training e test set
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        return X_train, X_test, y_train, y_test

    def train_model(self, X_train, y_train):
        """Creazione e allenamento del modello di regressione logistica"""
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        return model

    def evaluate_model(self, model, X_test, y_test):
        """Valutazione del modello con accuratezza e AUC"""
        y_pred = model.predict(X_test)
        y_pred_prob = model.predict_proba(X_test)[:, 1]  # Probabilità di churn (1)

        accuracy = accuracy_score(y_test, y_pred)
        auc = roc_auc_score(y_test, y_pred_prob)
        cm = confusion_matrix(y_test, y_pred)

        # Stampa delle metriche
        print(f"Accuratezza del modello: {accuracy:.4f}")
        print(f"AUC del modello: {auc:.4f}")
        print(f"Matrice di confusione:\n{cm}")
        
        # Curva ROC
        fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
        
        plt.figure(figsize=(8, 6))
        plt.plot(fpr, tpr, color='b', label=f'ROC Curve (AUC = {auc:.4f})')
        plt.plot([0, 1], [0, 1], color='r', linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Curva ROC')
        plt.legend(loc='lower right')
        plt.show()

    def run_analysis(self):
        """Esegui tutta l'analisi: carica, pulisce, prepara i dati, allena e valuta il modello"""
        # Fase 1: Esplorazione dei dati
        self.show_df_info()
        self.show_stat()
        self.show_churn_distribution()

        # Fase 2: Pulizia dei dati
        self.clean_data()

        # Fase 3: Feature Engineering
        self.feature_engineering()

        # Fase 4: Preparazione dei dati per il modello
        X_train, X_test, y_train, y_test = self.prepare_data()

        # Fase 5: Allenamento del modello
        model = self.train_model(X_train, y_train)

        # Fase 6: Valutazione del modello
        self.evaluate_model(model, X_test, y_test)

# Creazione dell'oggetto e esecuzione dell'analisi
file_path = 'dataset_clienti_churn_pulito.csv'
churn_model = ChurnPrediction(file_path)
churn_model.run_analysis()
