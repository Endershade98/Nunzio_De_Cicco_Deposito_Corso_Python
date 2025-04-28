import pandas as pd


class StatisticalAnalyzer:
    """Classe per l'analisi statistica di un DataFrame pandas.
    Si concentra sulle colonne numeriche."""
    def __init__(self, df: pd.DataFrame):
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Il dato deve essere un DataFrame pandas.")
        self.df = df.select_dtypes(include='number')  # Considera solo colonne numeriche

    def mean(self):
        """Media per colonna numerica"""
        return self.df.mean()

    def median(self):
        """Mediana per colonna numerica"""
        return self.df.median()

    def std_dev(self):
        """Deviazione standard"""
        return self.df.std()

    def variance(self):
        """Varianza"""
        return self.df.var()

    def min_value(self):
        """Valori minimi"""
        return self.df.min()

    def max_value(self):
        """Valori massimi"""
        return self.df.max()

    def correlation(self):
        """Matrice di correlazione"""
        return self.df.corr()

    def covariance(self):
        """Matrice di covarianza"""
        return self.df.cov()

    def summary(self):
        """Riepilogo statistico tipo describe(), ma personalizzato"""
        return pd.DataFrame({
            'mean': self.mean(),
            'std_dev': self.std_dev(),
            'min': self.min_value(),
            'max': self.max_value(),
            'variance': self.variance(),
            'median': self.median()
        })

