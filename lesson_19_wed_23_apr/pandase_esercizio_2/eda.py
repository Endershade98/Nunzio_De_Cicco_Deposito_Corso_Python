import pandas as pd

# Caricamento del file già pulito
df = pd.read_csv("dataset_clienti_churn_pulito.csv")

class EDA:
    
    def __init__(self, cleaned_df):
        self.df = cleaned_df
        
    def new_column(self):
        """Nuova colonna: Costo per GB"""
        self.df['Costo_per_GB'] = self.df.apply(
            lambda row: row['Tariffa_Mensile'] / row['Dati_Consumati'] if row['Dati_Consumati'] > 0 else 0,
            axis=1
        )

    def analize_grouped_data(self):
        """Analisi con groupby()"""
        grouped = self.df.groupby('Churn')[['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Costo_per_GB']].mean()
        print("\nStatistiche medie per clienti che hanno lasciato o meno (Churn):")
        print(grouped)

    def count_churn(self):
        """Conteggio Churn per classi di età"""
        self.df['Classe_Età'] = pd.cut(self.df['Età'], bins=[0, 25, 45, 65, 100], labels=['Giovani', 'Adulti', 'Maturi', 'Senior'])
        churn_per_eta = self.df.groupby(['Classe_Età', 'Churn']).size().unstack(fill_value=0)
        print("\nDistribuzione Churn per fascia d'età:")
        print(churn_per_eta)

    def correlation_matrix(self):
        """Matrice di correlazione"""
        corr = self.df[['Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 'Dati_Consumati',
                        'Servizio_Clienti_Contatti', 'Costo_per_GB']].corr()
        print("\nMatrice di correlazione:")
        print(corr)
