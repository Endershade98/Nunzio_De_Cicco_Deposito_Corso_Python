import numpy as np
from progetto_musica.statistical_analysis import StatisticalAnalyzer
from msql_test_db import crea_tabelle_studenti, estrai_dati_numerici


# Crea il database e popola le tabelle
crea_tabelle_studenti()

# Estrai i dati dalla tabella 'studenti_voti_classe_a'
dati_classe_a = estrai_dati_numerici("studenti_voti_classe_a")
# Estrai i dati dalla tabella 'studenti_voti_classe_b'
dati_classe_b = estrai_dati_numerici("studenti_voti_classe_b")
# Estrai i dati dalla tabella 'studenti_voti_classe_c'
dati_classe_c = estrai_dati_numerici("studenti_voti_classe_c")


# Array di testing 
datasets = {
    "1": dati_classe_a,
    "2": dati_classe_b,
    "3": dati_classe_c
}

# Manda a schermo il menu con le operazioni che posso eseguire
def show_menu():
    print("\nSeleziona un'operazione:")
    print("1. Media")
    print("2. Mediana")
    print("3. Deviazione standard")
    print("4. Varianza")
    print("5. Minimo")
    print("6. Massimo")
    print("7. Correlazione")
    print("8. Covarianza")
    print("9. Riepilogo statistico")
    print("0. Esci")

# funzione principale
def main():
    # Mandare a schermo le scelte di datasets/ tabelle disponibili
    print("Benvenuto! Seleziona un dataset da analizzare:")
    for key, val in datasets.items():
        print(f"{key}: array di forma {val.shape}")
    
    # Selezionare il dataset
    scelta_dataset = input("Inserisci il numero del dataset/tabella da analizzare (1-3): ").strip()
    if scelta_dataset not in datasets:
        print("Dataset non valido.")
        return
    # Istanzia la classe di analisi dei dati 
    analyzer = StatisticalAnalyzer(datasets[scelta_dataset])
    # Manda a schermo il dataset elezionato prima
    print("\nDataset selezionato:\n", analyzer.data) 
    
    # While loop per eseguire le operazioni di scelta
    while True:
        show_menu() # manda a schermo il menu
        scelta = input("Scegli un'opzione: ").strip() # seleziona un'operazione da eseguire
        axis = int(input("Select the axis (rows = 1, columns = 0): ")) # seleziono anche l'asse se serve
        
        if scelta == "1":
            print("Media per colonna:\n", analyzer.mean(axis))
        elif scelta == "2":
            print("Mediana per colonna:\n", analyzer.median(axis))
        elif scelta == "3":
            print("Deviazione standard:\n", analyzer.std_dev(axis))
        elif scelta == "4":
            print("Varianza:\n", analyzer.variance(axis))
        elif scelta == "5":
            print("Valori minimi:\n", analyzer.min_value(axis))
        elif scelta == "6":
            print("Valori massimi:\n", analyzer.max_value(axis))
        elif scelta == "7":
            print("Matrice di correlazione:\n", analyzer.correlation())
        elif scelta == "8":
            print("Matrice di covarianza:\n", analyzer.covariance())
        elif scelta == "9": # manda a schermo tutte le grandezze calcolate
            summary = analyzer.summary()
            for key, value in summary.items():
                print(f"{key}: {value}")
        elif scelta == "0":
            print("Uscita dal programma. Alla prossima!")
            break
        else:
            print("Scelta non valida. Riprova.")

# Entry point del codice
if __name__ == "__main__":
    main()
