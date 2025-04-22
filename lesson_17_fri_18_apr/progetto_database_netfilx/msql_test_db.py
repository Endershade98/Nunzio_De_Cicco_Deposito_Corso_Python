import mysql.connector
from mysql.connector import Error
import numpy as np



def crea_tabelle_studenti():
    try:
        # Connessione al server MySQL
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Allitterazione0098', 
        )

        if conn.is_connected():
            cursor = conn.cursor()
            
            # Creazione del database se non esiste
            cursor.execute("CREATE DATABASE IF NOT EXISTS scuola")
            print("Database 'scuola' creato o già esistente.")

        # Seleziona il database
        conn.database = 'scuola'

        cursor = conn.cursor()

        # -------------------- TABELLA A --------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS studenti_voti_classe_a (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50),
            corso VARCHAR(50),
            eta INT,
            voto FLOAT
        )
        """)
        print("Tabella 'studenti_voti_classe_a' creata o già esistente.")
        
        # Dati della tabella della classee a
        dati_a = [
            ("Anna", "Matematica", 19, 28.5),
            ("Luca", "Fisica", 20, 30.0),
            ("Marta", "Chimica", 21, 26.5),
            ("Paolo", "Matematica", 22, 29.0),
            ("Giulia", "Fisica", 20, 27.0)
        ]

        cursor.executemany("""
        INSERT INTO studenti_voti_classe_a (nome, corso, eta, voto)
        VALUES (%s, %s, %s, %s)
        """, dati_a)

        # -------------------- TABELLA B --------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS studenti_voti_classe_b (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50),
            corso VARCHAR(50),
            eta INT,
            voto FLOAT
        )
        """)
        print("Tabella 'studenti_voti_classe_b' creata o già esistente.")
        
        # Dati della tabella della classee b
        dati_b = [
            ("Marco", "Biologia", 19, 25.0),
            ("Sara", "Fisica", 20, 30.0),
            ("Elena", "Matematica", 18, 27.5),
            ("Davide", "Chimica", 21, 24.0),
            ("Irene", "Biologia", 20, 26.0)
        ]

        cursor.executemany("""
        INSERT INTO studenti_voti_classe_b (nome, corso, eta, voto)
        VALUES (%s, %s, %s, %s)
        """, dati_b)

        # -------------------- TABELLA C --------------------
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS studenti_voti_classe_c (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(50),
            corso VARCHAR(50),
            eta INT,
            voto FLOAT
        )
        """)
        print("Tabella 'studenti_voti_classe_c' creata o già esistente.")
        
        # Dati della tabella della classee c
        dati_c = [
            ("Giorgio", "Informatica", 22, 29.0),
            ("Francesca", "Statistica", 21, 30.0),
            ("Simone", "Informatica", 23, 28.0),
            ("Laura", "Matematica", 22, 27.5),
            ("Alessio", "Fisica", 20, 26.0)
        ]

        cursor.executemany("""
        INSERT INTO studenti_voti_classe_c (nome, corso, eta, voto)
        VALUES (%s, %s, %s, %s)
        """, dati_c)

        # Salvataggio delle modifiche
        conn.commit()
        print("Dati inseriti correttamente in tutte le tabelle.")

    except Error as e:
        print("Errore durante la creazione o popolamento del database:", e)

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("Connessione MySQL chiusa.")


def estrai_dati_numerici(tabella):
    try:
        # Riapre la connessione al server MySQL e al database 'scuola'
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Allitterazione0098',
            database='scuola' # database creato in precedenza
        )
        # Connessione al cursore
        cursor = conn.cursor()
        
        # Seleziona solo le colonne numeriche: eta, voto
        query = f"SELECT eta, voto FROM {tabella}"
        cursor.execute(query)
        risultati = cursor.fetchall()

        # Conversione in array NumPy 2D con elementi di tipo float
        array_dati = np.array(risultati, dtype=float)
        # Output array numerico
        return array_dati

    except mysql.connector.Error as e:
        print("Errore durante l'estrazione:", e)
        return np.array([])

    finally: 
        # Chiusura cursore e connessione
        if conn.is_connected():
            cursor.close()
            conn.close()

