import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


class DataSimulator:
    """Rappresenta un generatore di dati per i visitatori di un parco"""
    def __init__(self, giorni=365, media=2000, deviazione=500, trend_giornaliero=2):
        self.giorni = giorni
        self.media = media # la media che decido di impostare
        self.deviazione = deviazione # la deviazione standard che decido di impostare
        self.trend_giornaliero = trend_giornaliero # il trend che calcolo per giorno
        self.df = None # default a None

    def genera_data_frame_visitatori(self):
        """restituisce il dataframe dei visitatori"""
        np.random.seed(42)
        giorni_arr = np.arange(self.giorni)
        trend = giorni_arr * self.trend_giornaliero # 2 al giorno
        rumore = np.random.normal(loc=0, scale=self.deviazione, size=self.giorni)
        visitatori = self.media + trend + rumore
        date = pd.date_range(start="2025-01-01", periods=self.giorni) # creare le date
        self.df = pd.DataFrame({'visitatori': visitatori}, index=date) # creare il df
        return self.df


class VisitorsAnalyzer:
    """Rappresenta un analizzatore dei dati di un dataframe"""
    def __init__(self, df):
        self.df = df
        self.df_mensile = None

    def aggiungi_media_mobile(self, finestra=7):
        self.df['media_mobile_7gg'] = self.df['visitatori'].rolling(window=finestra).mean()
        return self.df

    def calcola_statistiche_mensili(self):
        self.df_mensile = self.df['visitatori'].resample('M').agg(['mean', 'std'])
        return self.df_mensile

    def salva_csv(self, path_dati='visitatori_parco_2024.csv', path_mensile='visitatori_parco_mensile.csv'):
        self.df.to_csv(path_dati, index_label='data')
        if self.df_mensile is not None:
            self.df_mensile.to_csv(path_mensile, index_label='mese')


class VisitorsViewer:
    """Rappresenta un visualizzatore di dati"""
    def __init__(self, df, df_mensile=None):
        self.df = df
        self.df_mensile = df_mensile # settato a None

    def grafico_giornaliero_con_media_mobile(self):
        plt.figure(figsize=(14, 6))
        plt.plot(self.df.index, self.df['visitatori'], label='Visitatori Giornalieri', color='lightblue')
        plt.plot(self.df.index, self.df['media_mobile_7gg'], label='Media Mobile (7 giorni)', color='blue', linewidth=2)
        plt.title("Visitatori Giornalieri con Media Mobile Settimanale")
        plt.xlabel("Data")
        plt.ylabel("Numero di Visitatori")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def grafico_media_mensile(self):
        if self.df_mensile is not None:
            plt.figure(figsize=(12, 5))
            plt.plot(self.df_mensile.index, self.df_mensile['mean'], marker='o', color='darkgreen')
            plt.title("Media Mensile dei Visitatori")
            plt.xlabel("Mese")
            plt.ylabel("Visitatori Medi")
            plt.grid(True)
            plt.tight_layout()
            plt.show()

def menu():
    # Istanzio le variabili che useremo durante il menu
    generatore = DataSimulator()
    df = None
    analisi = None
    df_mensile = None
    visual = None

    # Loop del menu principale
    while True:
        print("\nMENU ANALISI DATI VISITATORI")
        print("1. Genera dati simulati")
        print("2. Aggiungi media mobile (7 giorni)")
        print("3. Calcola media e deviazione mensile")
        print("4. Salva dati su file CSV")
        print("5. Mostra grafico giornaliero con media mobile")
        print("6. Mostra grafico della media mensile")
        print("0. Esci")

        scelta = input("Seleziona un'opzione: ")

        # Opzione 1: generazione dati
        if scelta == "1":
            df = generatore.genera_data_frame_visitatori()
            print("Dati generati con successo.")

        # Opzione 2: aggiunta media mobile
        elif scelta == "2":
            if df is None:
                print("Errore: devi prima generare i dati (opzione 1).")
            else:
                analisi = VisitorsAnalyzer(df)
                df = analisi.aggiungi_media_mobile()
                print("Media mobile a 7 giorni aggiunta.")

        # Opzione 3: calcolo statistiche mensili
        elif scelta == "3":
            if df is None:
                print("Errore: prima devi generare i dati.")
            else:
                if analisi is None:
                    analisi = VisitorsAnalyzer(df)
                df_mensile = analisi.calcola_statistiche_mensili()
                print("Statistiche mensili calcolate.")

        # Opzione 4: salvataggio su CSV
        elif scelta == "4":
            if analisi is None:
                print("Errore: devi prima effettuare l'analisi.")
            else:
                analisi.salva_csv()
                print("Dati salvati su file CSV.")

        # Opzione 5: visualizzazione grafico giornaliero
        elif scelta == "5":
            if df is None or 'media_mobile_7gg' not in df.columns:
                print("Errore: prima devi generare i dati e aggiungere la media mobile.")
            else:
                visual = VisitorsViewer(df, df_mensile)
                visual.grafico_giornaliero_con_media_mobile()

        # Opzione 6: visualizzazione grafico mensile
        elif scelta == "6":
            if df_mensile is None:
                print("Errore: devi prima calcolare le statistiche mensili.")
            else:
                visual = VisitorsViewer(df, df_mensile)
                visual.grafico_media_mensile()

        # Uscita dal programma
        elif scelta == "0":
            print("Uscita dal programma.")
            break

        # Scelta non valida
        else:
            print("Scelta non valida. Inserisci un numero tra 0 e 6.")

# Esecuzione del menu principale
if __name__ == "__main__":
    menu()
