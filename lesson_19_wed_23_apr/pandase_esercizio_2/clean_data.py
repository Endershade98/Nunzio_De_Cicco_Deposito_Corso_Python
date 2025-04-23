import pandas as pd
import numpy as np
from load_data import DataLoader

# Istanzia DataLoader per caricare i dati da pulire
loaded_data = DataLoader()
df_loaded = loaded_data.df

class DataCleaner:
    
    def __init__(self, loaded_df):
        self.df = loaded_df  # usa il dataframe caricato in DataLoader
    
    def remove_duplicate_rows(self): 
        """Rimozione righe duplicate (se presenti)"""
        self.df = self.df.drop_duplicates()
        return self.df
    
    def remove_nan(self):
        """Rimozione righe con tutti i valori NaN"""
        self.df = self.df.dropna(how='all')
        return self.df
    
    def substitute_values(self):
        """Sostituzione dei valori mancanti per colonne numeriche con la mediana"""
        colonne_numeriche = ['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati', 'Servizio_Clienti_Contatti']
        for col in colonne_numeriche:
            if col in self.df.columns and self.df[col].isnull().any():
                self.df[col].fillna(self.df[col].median(), inplace=True)
        return self.df
    
    def remove_age_junk_data(self):
        """Correzione anomalie nei dati per l'età"""
        self.df = self.df[(self.df['Età'] >= 0) & (self.df['Età'] <= 100)]
        return self.df
    
    def remove_fee_junk_data(self):
        """Correzione anomalie nei dati per le tariffe mensili"""
        self.df = self.df[(self.df['Tariffa_Mensile'] >= 5) & (self.df['Tariffa_Mensile'] <= 200)]
        return self.df
    
    def remove_consumed_data(self):
        """Rimozione valori negativi nei dati consumati"""
        self.df = self.df[self.df['Dati_Consumati'] >= 0]
        return self.df
    
    def filter_client_service(self):
        """Filtra il servizio clienti"""
        self.df = self.df[self.df['Servizio_Clienti_Contatti'] >= 0]
        self.df['Servizio_Clienti_Contatti'] = self.df['Servizio_Clienti_Contatti'].astype(int)
        return self.df
