import numpy as np


class ArrayManager:
    def __init__(self):
        self.array = None # inizializzato a None

    def crea_array_random(self, lunghezza=15, minimo=1, massimo=100):
        """Crea un array di numeri interi casuali tra minimo e massimo"""
        if minimo == massimo:
            raise ValueError(f"{minimo} e {massimo} devono essere diversi")
        else:
            self.array = np.random.randint(minimo, massimo + 1, lunghezza)
            print("Array generato:")
        return self.array

    def somma_array(self):
        """Calcola e stampa la somma degli elementi"""
        if self.array is None:
            raise "Errore: crea prima l'array."
        else:
            return "Somma degli elementi:", np.sum(self.array)

    def media_array(self):
        """Calcola e stampa la media degli elementi"""
        if self.array is None:
            raise "Errore: crea prima l'array."
        else:
            return "Media degli elementi:", np.mean(self.array)

def menu():
    gestore = ArrayManager() # inizializza il gestore

    while True:
        print("\n--- MENU ---")
        print("1. Crea array casuale")
        print("2. Calcola somma")
        print("3. Calcola media")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            try:
                lunghezza = int(input("Lunghezza array: "))
                minimo = int(input("Valore minimo: "))
                massimo = int(input("Valore massimo: "))
                gestore.crea_array_random(lunghezza, minimo, massimo)
            except ValueError:
                print("Input non valido. Inserisci solo numeri interi.")

        elif scelta == "2":
            gestore.somma_array()

        elif scelta == "3":
            gestore.media_array()

        elif scelta == "0":
            print("Uscita dal programma.")
            break

        else:
            print("Opzione non valida. Riprova.")

# Avvio programma
if __name__ == "__main__":
    menu()
