from analizer import StatisticalAnalyzer


def menu():
    """Funzione che mostra un menu interattivo per eseguire analisi statistiche
       sui dati inseriti dall'utente.
    """
    # Richiede all'utente di inserire una lista di numeri separati da virgola
    data = input("Inserisci una lista di numeri separati da virgola (es: 1,2,3,4):\n")
    
    try:
        # Converte la stringa in una lista di numeri float (rimuovendo gli spazi extra)
        data_list = [float(x.strip()) for x in data.split(",")]
    except ValueError:
        # Se l'utente inserisce valori non numerici, viene sollevato un errore
        print("Errore: assicurati di inserire solo numeri.")
        return  # Interrompe l'esecuzione della funzione nel caso di errore

    # Crea un oggetto della classe StatisticalAnalyzer con i dati forniti dall'utente
    analyzer = StatisticalAnalyzer(data_list)

    # Definisce le opzioni del menu, associando ogni numero a una funzione specifica
    options = {
        "1": ("Media", analyzer.mean),
        "2": ("Mediana", analyzer.median),
        "3": ("Moda", analyzer.mode),
        "4": ("Varianza", analyzer.variance),
        "5": ("Deviazione Standard", analyzer.standard_deviation),
        "6": ("Minimo", analyzer.min),
        "7": ("Massimo", analyzer.max),
        "8": ("Riassunto", analyzer.summary),
        "9": ("Esci", None)  # Opzione per uscire dal programma
    }

    # Ciclo per mostrare il menu finché l'utente non sceglie di uscire
    while True:
        print("\n--- Menu Analisi Statistica ---")
        # Mostra tutte le opzioni disponibili nel menu
        for key, (desc, _) in options.items():
            print(f"{key}. {desc}")
        
        # Richiede all'utente di scegliere un'opzione
        choice = input("Seleziona un'opzione: ")

        if choice == "9":
            # Se l'utente sceglie "9", esce dal programma
            print("Uscita dal programma.")
            break  # Interrompe il ciclo e chiude il programma
        elif choice in options:
            # Se l'utente seleziona una delle opzioni valide
            try:
                # Esegue la funzione associata all'opzione scelta
                result = options[choice][1]()
                print(f"\nRisultato di '{options[choice][0]}':\n{result}")
            except Exception as e:
                # Gestisce eventuali errori durante l'esecuzione della funzione
                print(f"Errore durante l'esecuzione: {e}")
        else:
            # Se l'utente inserisce un'opzione non valida
            print("Opzione non valida, riprova.")  # Richiesta di input valido

# Se il file viene eseguito direttamente (non importato), avvia il menu
if __name__ == "__main__":
    menu()
