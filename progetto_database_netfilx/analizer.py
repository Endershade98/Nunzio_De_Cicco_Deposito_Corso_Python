import numpy as np 


class StatisticalAnalyzer:
    def __init__(self, data):
        """
        Inizializza l'oggetto con un array di dati numerici.
        Converte i dati in un array NumPy di tipo float.
        """
        self.data = np.array(data, dtype=float)

    def mean(self):
        """Restituisce la media aritmetica dei dati."""
        return np.mean(self.data)

    def median(self):
        """Restituisce la mediana dei dati."""
        return np.median(self.data)

    def mode(self):
        """Calcola la moda (valore più frequente). Se più valori 
        hanno la stessa frequenza massima, li restituisce tutti.
        """
        values, counts = np.unique(self.data, return_counts=True)
        max_count = np.max(counts)
        modes = values[counts == max_count]
        return modes if len(modes) > 1 else modes[0]

    def variance(self):
        """Restituisce la varianza (dispersione dei dati)."""
        return np.var(self.data)

    def standard_deviation(self):
        """Restituisce la deviazione standard."""
        return np.std(self.data)

    def min(self):
        """Restituisce il valore minimo nei dati."""
        return np.min(self.data)

    def max(self):
        """Restituisce il valore massimo nei dati."""
        return np.max(self.data)

    def summary(self):
        """Restituisce un dizionario con tutte le statistiche principali."""
        return {
            "media": self.mean(),
            "mediana": self.median(),
            "moda": self.mode(),
            "varianza": self.variance(),
            "deviazione_standard": self.standard_deviation(),
            "minimo": self.min(),
            "massimo": self.max()
        }
