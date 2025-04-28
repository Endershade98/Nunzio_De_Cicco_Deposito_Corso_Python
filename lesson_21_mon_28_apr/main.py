from lesson_21_mon_28_apr.classification import WineClassifier

# Menu a tendina per l'esecuzione dei metodi
def menu():
    wine_classifier = WineClassifier()

    while True:
        print("\n--- Menu ---")
        print("1. Esplora il dataset")
        print("2. Riduci la dimensionalità con PCA")
        print("3. Allena il modello")
        print("4. Valuta il modello")
        print("5. Visualizza l'importanza delle feature")
        print("6. Visualizza la matrice di confusione")
        print("7. Ottimizza il modello")
        print("8. Esci")
        
        choice = input("Scegli un'opzione (1-8): ")

        if choice == '1':
            wine_classifier.explore_data()
        elif choice == '2':
            wine_classifier.reduce_dimensionality()
        elif choice == '3':
            wine_classifier.train_model()
        elif choice == '4':
            wine_classifier.evaluate_model()
        elif choice == '5':
            wine_classifier.feature_importance()
        elif choice == '6':
            wine_classifier.confusion_matrix()
        elif choice == '7':
            wine_classifier.optimize_model()
        elif choice == '8':
            print("Uscita...")
            break
        else:
            print("Scelta non valida. Riprova.")


# Entry point 
if __name__ == '__main__':
    # Esegui il menu
    menu()