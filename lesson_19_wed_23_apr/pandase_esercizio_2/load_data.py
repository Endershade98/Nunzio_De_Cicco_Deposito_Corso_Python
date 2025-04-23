import pandas as pd
import numpy as np
import os

file_path = '/home/endershade/Desktop/Python_Course_Repo/lesson_19_wed_23_apr/pandase_esercizio_2/dataset_clienti_churn_dirty.csv'

class DataLoader:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = self.load_data()
    
    def load_data(self):
        """Carica il file CSV in un DataFrame."""
        if not os.path.exists(self.file_path):
            print(f"Errore: il file '{self.file_path}' non esiste.")
            return pd.DataFrame()  # restituisce un DataFrame vuoto
        try:
            df = pd.read_csv(self.file_path)
            print(f"File '{self.file_path}' caricato con successo.")
            return df
        except Exception as e:
            print(f"Errore nel caricamento del file: {e}")
            return pd.DataFrame()

    def show_df_info(self):
        """Mostra informazioni generali sulle colonne (tipo, valori nulli, memoria)"""
        print("\nInfo dataset:")
        print(self.df.info())
        
    def show_stat(self):
        """Statistiche descrittive per colonne numeriche"""
        print("\nStatistiche descrittive:")
        print(self.df.describe())
        
    def show_churn(self):
        """Distribuzione dei valori unici per colonne categoriche o interessanti"""
        if "Churn" in self.df.columns:
            print("\nDistribuzione 'Churn':")
            print(self.df["Churn"].value_counts())
        else:
            print("Colonna 'Churn' non trovata.")

        if "Servizio_Clienti_Contatti" in self.df.columns:
            print("\nDistribuzione 'Servizio_Clienti_Contatti':")
            print(self.df["Servizio_Clienti_Contatti"].value_counts())
        else:
            print("Colonna 'Servizio_Clienti_Contatti' non trovata.")
