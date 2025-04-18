import numpy as np

def stampa_risultato(func):
    """
    Decoratore per stampare il risultato di una funzione che restituisce un valore.
    """
    def wrapper(self, *args, **kwargs):
        risultato = func(self, *args, **kwargs)
        if risultato is not None:
            print(risultato)
    return wrapper

class MatricePersonalizzata:
    def __init__(self):
        self.matrix = self.crea_matrice_personalizzata()

    def crea_matrice_personalizzata(self):
        print("=== CONFIGURAZIONE MATRICE ===")
        while True:
            try:
                start = int(input("Inserisci il valore iniziale (start): "))
                stop = int(input("Inserisci il valore finale (stop): "))
                step = int(input("Inserisci il passo (step): "))

                elementi = len(range(start, stop, step))
                print(f"Totale elementi generabili: {elementi}")

                shape_input = input("Inserisci la forma desiderata (es. 6x6 o 3x12): ")
                rows, cols = map(int, shape_input.lower().split("x"))

                if rows * cols != elementi:
                    print("Errore: la forma non combacia con il numero di elementi.")
                    continue

                values = list(range(start, stop, step))
                matrix = np.array(values).reshape((rows, cols))
                print("Matrice generata correttamente.")
                return matrix

            except Exception as e:
                print(f"Errore: {e}")
                print("Riprova.\n")

    @stampa_risultato
    def mostra_matrice(self):
        return self.matrix

    @stampa_risultato
    def inverti_matrice(self):
        return self.matrix[::-1]

    @stampa_risultato
    def diagonale_invertita(self):
        min_dim = min(self.matrix.shape)
        rev = self.matrix[::-1]
        return np.array([rev[i][i] for i in range(min_dim)])

    @stampa_risultato
    def sub_matrice(self):
        if self.matrix.shape[0] < 3 or self.matrix.shape[1] < 5:
            print("Matrice troppo piccola per estrarre la sub-matrice [1:3, 2:5].")
            return
        return self.matrix[1:3, 2:5]

    @stampa_risultato
    def filtro_colonne_mod3(self):
        cols = [x for x in range(self.matrix.shape[1]) if x % 3 == 0]
        return self.matrix[::-1][:, cols]


def mostra_menu(matrice_obj):
    operazioni = {
        "1": ("Mostra matrice originale", matrice_obj.mostra_matrice),
        "2": ("Matrice invertita", matrice_obj.inverti_matrice),
        "3": ("Diagonale invertita", matrice_obj.diagonale_invertita),
        "4": ("Sub-matrice (1:3, 2:5)", matrice_obj.sub_matrice),
        "5": ("Filtro colonne %3", matrice_obj.filtro_colonne_mod3),
        "0": ("Esci", None)
    }

    while True:
        print("\n--- MENU ---")
        for key, (desc, _) in operazioni.items():
            print(f"{key}. {desc}")
        scelta = input("Scegli un'opzione: ").strip()

        if scelta in operazioni:
            if scelta == "0":
                print("Uscita dal programma.")
                break
            else:
                funzione = operazioni[scelta][1]
                funzione()
        else:
            print("Scelta non valida. Riprova.")

# --- Programma principale ---
matrice = MatricePersonalizzata()
mostra_menu(matrice)
