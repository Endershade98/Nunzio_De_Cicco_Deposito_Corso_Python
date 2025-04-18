from progetto_database_netfilx.statistical_analysis import StatisticalAnalyzer

# Funzione per mostrare il menu e ottenere la scelta dell'utente
def mostra_menu():
    print("\nSeleziona una statistica da calcolare:")
    print("1. Media")
    print("2. Mediana")
    print("3. Deviazione Standard")
    print("4. Varianza")
    print("5. Minimo")
    print("6. Massimo")
    
    scelta_statistica = int(input("Inserisci il numero della statistica che vuoi calcolare: "))
    
    print("\nSeleziona l'asse su cui calcolare (0 = Colonne, 1 = Righe):")
    axis = int(input("Inserisci l'asse (0 per colonne, 1 per righe): "))
    
    return scelta_statistica, axis

# Funzione per calcolare la statistica selezionata
def calcola_statistica(sceltastatistica, axis):
    # Dati di esempio (array 2D)
    data = [
        [25, 45000],
        [30, 50000],
        [22, 40000],
        [35, 55000],
        [28, 47000]
    ]
    
    analisi = StatisticalAnalyzer(data)
    
    if sceltastatistica == 1:
        result = analisi.mean(axis)
        stat_name = "Media"
    elif sceltastatistica == 2:
        result = analisi.median(axis)
        stat_name = "Mediana"
    elif sceltastatistica == 3:
        result = analisi.std_dev(axis)
        stat_name = "Deviazione Standard"
    elif sceltastatistica == 4:
        result = analisi.variance(axis)
        stat_name = "Varianza"
    elif sceltastatistica == 5:
        result = analisi.min_value(axis)
        stat_name = "Minimo"
    elif sceltastatistica == 6:
        result = analisi.max_value(axis)
        stat_name = "Massimo"
    else:
        print("Scelta non valida!")
        return
    
    print(f"\n{stat_name} su asse {axis}:\n{result}")

# Funzione principale che esegue tutto il processo
def main():
    print("Benvenuto nell'analizzatore statistico!")
    
    # Mostra il menu e ottieni le scelte
    scelta_statistica, axis = mostra_menu()
    
    # Calcola la statistica e mostra il risultato
    calcola_statistica(scelta_statistica, axis)

# entry point per il codice
if __name__ == "__main__":
    main()
