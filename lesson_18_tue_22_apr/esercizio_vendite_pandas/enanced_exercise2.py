import pandas as pd


class AnalisiVendite:
    """rappresenta una classe di gestione delle vendite"""
    def __init__(self, file_path):
        # Carica il file CSV e crea la colonna "Totale Vendite"
        self.df = pd.read_csv(file_path)
        self.df["Totale Vendite"] = self.df["Quantità"] * self.df["Prezzo Unitario"]

    def totale_per_prodotto(self):
        """calcola il totale delle vendite per prodotto"""
        return self.df.groupby("Prodotto")["Totale Vendite"].sum().reset_index()

    def prodotto_piu_venduto(self):
        """calcola il prodotto più venduto per quantità"""
        return self.df.groupby("Prodotto")["Quantità"].sum().idxmax()

    def citta_maggior_vendite(self):
        """restituisce la città con il maggior volume di vendite totali"""
        return self.df.groupby("Città")["Totale Vendite"].sum().idxmax()

    def vendite_superiori(self, soglia=1000):
        """nuovo DataFrame con vendite superiori a 1000 euro"""
        return self.df[self.df["Totale Vendite"] > soglia]

    def ordinato_per_totale(self):
        """ordina il DataFrame originale per "Totale Vendite" in ordine decrescente"""
        return self.df.sort_values(by="Totale Vendite", ascending=False)

    def conteggio_per_citta(self):
        """numero di vendite per ogni città"""
        return self.df["Città"].value_counts()

    def stampa_analisi(self):
        """stampa tutti i risultati dell'analisi"""
        print("\nTotale vendite per prodotto:")
        print(self.totale_per_prodotto())

        print("\nProdotto più venduto per quantità:")
        print(self.prodotto_piu_venduto())

        print("\nCittà con il maggior volume di vendite totali:")
        print(self.citta_maggior_vendite())

        print("\nPrime 5 vendite superiori a 1000€:")
        print(self.vendite_superiori().head())

        print("\nPrime 5 righe ordinate per Totale Vendite:")
        print(self.ordinato_per_totale().head())

        print("\nNumero di vendite per ogni città:")
        print(self.conteggio_per_citta())


class MenuInterattivo:
    """rappresenta un menu interattivo che chiama i metodi della classe AnalisiVendite"""
    def __init__(self, analisi: AnalisiVendite):
        self.analisi = analisi # istanza di AnalisiVendite

    def mostra_menu(self):
        """avvia un menu a tendina con un while loop"""
        while True:
            print("\n--- MENU ---")
            print("1. Seleziona Pivot: Prodotto")
            print("2. Seleziona Pivot: Città")
            print("3. Esegui analisi: Totale vendite per prodotto")
            print("4. Esegui analisi: Prodotto più venduto per quantità")
            print("5. Esegui analisi: Città con maggior volume di vendite")
            print("6. Esegui analisi: Vendite superiori a 1000€")
            print("7. Esegui analisi: Ordinamento per Totale Vendite")
            print("8. Esegui analisi: Numero di vendite per città")
            print("9. Esci")
            scelta = input("Seleziona un'opzione (1-9): ")
  
            if scelta == '1':
                self.seleziona_pivot("Prodotto")
            elif scelta == '2':
                self.seleziona_pivot("Città")
            elif scelta == '3':
                self.analisi.stampa_analisi()
            elif scelta == '4':
                print(f"Prodotto più venduto per quantità: {self.analisi.prodotto_piu_venduto()}")
            elif scelta == '5':
                print(f"Città con maggior volume di vendite: {self.analisi.citta_maggior_vendite()}")
            elif scelta == '6':
                print("Vendite superiori a 1000€:")
                print(self.analisi.vendite_superiori())
            elif scelta == '7':
                print("Prime 5 righe ordinate per Totale Vendite:")
                print(self.analisi.ordinato_per_totale().head())
            elif scelta == '8':
                print("Numero di vendite per ogni città:")
                print(self.analisi.conteggio_per_citta())
            elif scelta == '9':
                print("Uscita dal programma.")
                break
            else:
                print("Scelta non valida. Riprova.")

    def seleziona_pivot(self, pivot_type):
        """permette di selezionare un pivot (Prodotto o Città) e stampare il risultato"""
        if pivot_type == "Prodotto":
            pivot = self.analisi.totale_per_prodotto()
            print("\nPivot selezionato: Totale Vendite per Prodotto")
            print(pivot)
        elif pivot_type == "Città":
            pivot = self.analisi.df.groupby("Città").agg({
                "Totale Vendite": "sum",
                "Quantità": "sum"
            }).reset_index()
            print("\nPivot selezionato: Totale Vendite e Quantità per Città")
            print(pivot)


# esecuzione del programma
def main():
    file_path = "/home/endershade/Desktop/Python_Course_Repo/vendite_per_citta.csv"
    analisi = AnalisiVendite(file_path) # istanza di AnalisiVendite
    menu = MenuInterattivo(analisi) # istanza di MenuInterattivo
    menu.mostra_menu() # manda a schermo il menu
    
    
# Entry point del codice con use case
if __name__ == "__main__":
    main()
