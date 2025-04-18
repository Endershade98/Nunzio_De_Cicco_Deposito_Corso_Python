import numpy as np


class StatisticalAnalyzer:
    
    def __init__(self, data):
        # Data dovrebbe essere un array numpy 2D (rows x columns)
        self.data = np.array(data)
        
    def mean(self, axis=0):
        """Calcola la media dei dati lungo un determinato asse.
        Axis=0 per media per colonna, Axis=1 per media per riga."""
        return np.mean(self.data, axis=axis)
    
    def median(self, axis=0):
        """Calcola la mediana dei dati lungo un determinato asse.
        Axis=0 per mediana per colonna, Axis=1 per mediana per riga."""
        return np.median(self.data, axis=axis)
    
    def std_dev(self, axis=0):
        """Calcola la deviazione standard dei dati lungo un determinato asse.
        Axis=0 per deviazione standard per colonna, Axis=1 per deviazione standard per riga."""
        return np.std(self.data, axis=axis)
    
    def variance(self, axis=0):
        """Calcola la varianza dei dati lungo un determinato asse.
        Axis=0 per varianza per colonna, Axis=1 per varianza per riga."""
        return np.var(self.data, axis=axis)
    
    def min_value(self, axis=0):
        """Restituisce il valore minimo dei dati lungo un determinato asse.
        Axis=0 per minimo per colonna, Axis=1 per minimo per riga."""
        return np.min(self.data, axis=axis)
    
    def max_value(self, axis=0):
        """Restituisce il valore massimo dei dati lungo un determinato asse.
        Axis=0 per massimo per colonna, Axis=1 per massimo per riga."""
        return np.max(self.data, axis=axis)
    
    def correlation(self):
        """Calcola la matrice di correlazione tra le colonne (features) dei dati."""
        return np.corrcoef(self.data, rowvar=False)
    
    def covariance(self):
        """Calcola la matrice di covarianza tra le colonne (features) dei dati."""
        return np.cov(self.data, rowvar=False)

    def summary(self):
        """Riepilogo statistico: media, deviazione standard, min, max per ogni colonna."""
        return {
            'mean': self.mean(axis=0),
            'std_dev': self.std_dev(axis=0),
            'min': self.min_value(axis=0),
            'max': self.max_value(axis=0),
            'variance': self.variance(axis=0),
            'median': self.median(axis=0)
        }

