import mysql.connector
from collections import Counter
import numpy as np

class CategoricalDataAnalyzer:
    def __init__(self, host, user, password, database):
        """Inizializza la connessione al database."""
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.data_counter = None

    def fetch_and_count(self, query):
        """Esegue una query e conta le occorrenze dei valori."""
        self.cursor.execute(query)
        results = self.cursor.fetchall()

        # Flatten the results in caso di lista di tuple
        flat_results = [row[0] for row in results]

        # Conta le occorrenze
        self.data_counter = Counter(flat_results)

    def get_counts_array(self):
        """Restituisce un array NumPy con le frequenze dei valori."""
        if self.data_counter:
            counts_array = np.array(list(self.data_counter.values()))
            return counts_array
        else:
            raise ValueError("Nessun dato disponibile per l'analisi.")

    def get_labels(self):
        """Restituisce un array con le etichette univoche (categorie)."""
        if self.data_counter:
            return list(self.data_counter.keys())
        else:
            raise ValueError("Nessun dato disponibile.")

    def close_connection(self):
        """Chiude la connessione al database."""
        self.cursor.close()
        self.conn.close()
