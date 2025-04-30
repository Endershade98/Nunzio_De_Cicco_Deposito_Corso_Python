import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class DataPreprocessor:
    def __init__(self, file_path, target_column):
        """
        file_path: percorso del file CSV
        target_column: nome della colonna target (es. 'price')
        """
        self.file_path = file_path
        self.target_column = target_column
        self.df = None
        self.X = None
        self.y = None

    def load_data(self):
        """
        Carica il dataset da file CSV e mostra le prime righe e info generali.
        """
        self.df = pd.read_csv(self.file_path)
        print("Shape:", self.df.shape)
        print(self.df.head())
        print(self.df.info())

    def clean_data(self, drop_columns=None):
        """
        Rimuove colonne non necessarie e gestisce valori nulli.
        drop_columns: lista di colonne da rimuovere manualmente
        """
        if drop_columns:
            self.df.drop(columns=drop_columns, inplace=True)
        # Rimuove eventuali righe con valori nulli
        self.df.dropna(inplace=True)
        print(f"Dati dopo la pulizia: {self.df.shape}")

    def plot_correlations(self, top_n=10):
        """
        Calcola e mostra la matrice di correlazione rispetto alla variabile target.
        """
        corr = self.df.corr(numeric_only=True)
        top_corr = corr[self.target_column].abs().sort_values(ascending=False).head(top_n)
        print("Top correlazioni:\n", top_corr)

        plt.figure(figsize=(10, 8))
        sns.heatmap(self.df[top_corr.index].corr(), annot=True, cmap='coolwarm')
        plt.title("Heatmap delle correlazioni principali")
        plt.show()

    def split_features_target(self):
        """
        Divide il dataset in variabili indipendenti (X) e dipendente (y).
        """
        self.X = self.df.drop(columns=[self.target_column])
        self.y = self.df[self.target_column]
        return self.X, self.y
