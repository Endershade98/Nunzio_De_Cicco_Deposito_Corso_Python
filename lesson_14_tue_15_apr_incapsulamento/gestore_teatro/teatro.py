import posti_speciali as special

# Classe che rappresenta il teatro e gestisce i posti

class Teatro:
    """Teatro rappresenta il gestore dei posti di una sala teatrale"""
    def __init__(self):
        self._posti = []  # Lista di oggetti Posto (standard o VIP)

    def aggiungi_posto(self, numero, fila):
        """Aggiunge un nuovo posto alla lista, evitando duplicati."""
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                print(f"Posto {numero} nella fila {fila} esiste già.")
                return
        nuovo_posto = special.Posto(numero, fila)
        self._posti.append(nuovo_posto)
        print(f"Posto {numero} nella fila {fila} aggiunto.")

    def prenota_posto(self, numero, fila, prenotato=False):
        """Prenota un posto esistente, adattandosi al tipo di posto."""
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                if isinstance(posto, special.PostoStandard):
                    posto.prenota(prenotato)
                else:
                    posto.prenota() # prenota il posto
                return
        print(f"Posto {numero} nella fila {fila} non trovato.")

    def libera_posto(self, numero, fila):
        """Libera un posto specifico, se esiste."""
        for posto in self._posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.libera() # libera il posto
                return
        print(f"Posto {numero} nella fila {fila} non trovato.")

    def mostra_posti(self):
        """Stampa tutti i posti presenti, con stato occupazione."""
        if not self._posti:
            print("Nessun posto presente.")
            return
        posti_ordinati = sorted(self._posti, key=lambda p: (p.get_fila(), p.get_numero()))
        print("\nElenco posti:")
        for posto in posti_ordinati:
            stato = "Occupato" if posto.is_occupato() else "Libero"
            print(f"Fila {posto.get_fila()} - Posto {posto.get_numero()}: {stato}")


