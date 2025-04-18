import mysql.connector
from mysql.connector import Error
from collections import Counter
import numpy as np

class CategoricalDataAnalyzer:
    def __init__(self, host, user, password, database):
        """Inizializza la connessione al database."""
        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conn.cursor()
            self.data_counter = None
            print("Connessione al database riuscita.")
        except Error as e:
            print(f"Errore durante la connessione: {e}")
            self.conn = None
            self.cursor = None

    def fetch_and_count(self, query):
        """Esegue una query e conta le occorrenze dei valori."""
        if self.cursor is None:
            raise ConnectionError("Nessuna connessione attiva al database.")
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            flat_results = [row[0] for row in results]
            self.data_counter = Counter(flat_results)
            print("Dati analizzati correttamente.")
        except Error as e:
            print(f"Errore durante l'esecuzione della query: {e}")
            self.data_counter = None

    def get_counts_array(self):
        """Restituisce un array NumPy con le frequenze dei valori."""
        if self.data_counter:
            return np.array(list(self.data_counter.values()))
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
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
            print("Connessione chiusa.")
        except Error as e:
            print(f"Errore durante la chiusura della connessione: {e}")
