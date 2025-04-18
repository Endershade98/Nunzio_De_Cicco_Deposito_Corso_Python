import mysql.connector
import numpy as np


class RecordManager:
    def __init__(self, host, user, password, database):
        """Inizializza la connessione al database."""
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.data = None

    def fetch_data(self, query):
        """Esegue una query e memorizza i risultati come array NumPy."""
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        self.data = np.array(results, dtype=float)

    def calculate_mean(self):
        """Calcola la media dei dati."""
        if self.data is not None:
            return np.mean(self.data)
        else:
            raise ValueError("Nessun dato disponibile.")

    def calculate_median(self):
        """Calcola la mediana dei dati."""
        if self.data is not None:
            return np.median(self.data)
        else:
            raise ValueError("Nessun dato disponibile.")

    def calculate_variance(self):
        """Calcola la varianza dei dati."""
        if self.data is not None:
            return np.var(self.data)
        else:
            raise ValueError("Nessun dato disponibile.")

    def calculate_std_dev(self):
        """Calcola la deviazione standard dei dati."""
        if self.data is not None:
            return np.std(self.data)
        else:
            raise ValueError("Nessun dato disponibile.")

    def close_connection(self):
        """Chiude la connessione al database."""
        self.cursor.close()
        self.conn.close()
