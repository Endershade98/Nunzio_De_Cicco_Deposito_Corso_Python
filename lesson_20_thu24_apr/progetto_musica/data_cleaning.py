import pandas as pd


class DataCleaner:
    """Classe per la pulizia dei dati in un DataFrame pandas:
    gestione dei NaN, rimozione duplicati, conversione dei tipi e controllo dei valori unici."""
    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Il dato deve essere un DataFrame pandas.")
        self.df = df.copy()  # lavora sempre su una copia per sicurezza

    def drop_na(self, subset=None):
        """Rimuove le righe con valori nulli (opzionalmente solo in certe colonne)."""
        return self.df.dropna(subset=subset)

    def fill_na(self, strategy='mean', value=None):
        """
        Riempie i valori nulli secondo la strategia:
        - 'mean', 'median', 'mode' per colonne numeriche
        - oppure un valore fisso (`value`)
        """
        df_filled = self.df.copy() # crea prima una copia
        if value is not None:
            return df_filled.fillna(value)
        if strategy == 'mean': # inserisce la media come valore 
            return df_filled.fillna(df_filled.mean(numeric_only=True))
        elif strategy == 'median': # inserisce la mediana come valore
            return df_filled.fillna(df_filled.median(numeric_only=True))
        elif strategy == 'mode': # inserisce la moda come valore
            modes = df_filled.mode().iloc[0]
            return df_filled.fillna(modes)
        else:
            raise ValueError("Strategia non supportata. Usa: 'mean', 'median', 'mode' o specifica un valore.")

    def drop_duplicates(self, subset=None):
        """Rimuove i duplicati (intera riga o su colonne specifiche)."""
        return self.df.drop_duplicates(subset=subset)

    def convert_types(self, col_types: dict):
        """Converte il tipo delle colonne secondo il dizionario {colonna: tipo}."""
        return self.df.astype(col_types)

    def trim_strings(self):
        """Rimuove spazi all'inizio/fine da tutte le colonne di tipo stringa."""
        df_trimmed = self.df.copy()
        str_cols = df_trimmed.select_dtypes(include='object').columns
        df_trimmed[str_cols] = df_trimmed[str_cols].apply(lambda col: col.str.strip())
        return df_trimmed

    def remove_outliers_iqr(self, multiplier=1.5):
        """Rimuove gli outlier da tutte le colonne numeriche usando il metodo IQR."""
        df_numeric = self.df.select_dtypes(include='number')
        Q1 = df_numeric.quantile(0.25) # primo quartile 
        Q3 = df_numeric.quantile(0.75) # terzo quartile 
        IQR = Q3 - Q1 # normalizzazine
        mask = ~((df_numeric < (Q1 - multiplier * IQR)) | (df_numeric > (Q3 + multiplier * IQR))).any(axis=1)
        return self.df[mask]
    
    def get_unique_values(self):
        """Restituisce un dizionario con i valori unici per ogni colonna."""
        return {col: self.df[col].unique() for col in self.df.columns}
