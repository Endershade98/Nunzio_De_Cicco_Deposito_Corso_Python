import numpy as np

# Variabili globali per conservare i dati
array_lin = None
matrice_lin = None
matrice_random = None


def create(start=0, stop=1, step=12):
    """Crea un array di N numeri equidistanti tra start e stop"""
    global array_lin
    array_lin = np.linspace(start, stop, step)
    print("Array linspace (1D):")
    return array_lin

def update(rows=3, columns=4):
    """Cambia la forma dell'array in una matrice"""
    global array_lin, matrice_lin
    if array_lin is None:
        print("Errore: devi prima creare l'array con 'create'.")
        return
    try:
        matrice_lin = array_lin.reshape((rows, columns))
        print("\nMatrice linspace reshape:")
        print(matrice_lin)
    except ValueError:
        print("Errore: la forma non è compatibile con l'array originale.")

def randomize(rows=3, columns=4):
    """Genera una matrice casuale tra 0 e 1 di dimensione rows x columns"""
    global matrice_random
    matrice_random = np.random.rand(rows, columns)
    print("\nMatrice casuale:")
    print(matrice_random)

def calculate_sum(matrix_name): # utilizzare "lin" oppre "random"
    """Calcola e stampa la somma degli elementi della matrice indicata"""
    global matrice_lin, matrice_random
    if matrix_name == "lin":
        if matrice_lin is not None:
            print("Somma matrice linspace:", np.sum(matrice_lin))
        else:
            print("Matrice linspace non disponibile.")
    elif matrix_name == "random":
        if matrice_random is not None:
            print("Somma matrice casuale:", np.sum(matrice_random))
        else:
            print("Matrice casuale non disponibile.")
    else:
        print("Nome matrice non valido.")

# === Menu testuale ===
def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Crea array linspace")
        print("2. Cambia forma array in matrice")
        print("3. Genera matrice casuale")
        print("4. Calcola somma (linspace)")
        print("5. Calcola somma (random)")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            start = float(input("Start: "))
            stop = float(input("Stop: "))
            step = int(input("Numero di elementi: "))
            create(start, stop, step)

        elif scelta == "2":
            rows = int(input("Numero righe: "))
            columns = int(input("Numero colonne: "))
            update(rows, columns)

        elif scelta == "3":
            rows = int(input("Numero righe: "))
            columns = int(input("Numero colonne: "))
            randomize(rows, columns)

        elif scelta == "4":
            calculate_sum("lin")

        elif scelta == "5":
            calculate_sum("random")

        elif scelta == "0":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")
            break

# Esecuzione del menu
menu()
