from abc import ABC, abstractmethod

# interfaccia comune agli impiagati
class Impiegato(ABC):
    """Classe astratta per definire un Impiegato generico"""
    def __init__(self, nome: str, cognome: str, stipendio_base: float) -> None:
        self.nome = nome
        self.cognome = cognome
        self._stipendio = stipendio_base
        
    @abstractmethod
    def calcola_stipendio(self):
        pass
    
    @abstractmethod
    def get_stipendio(self):
        pass
    

class ImpiegatoFisso(Impiegato):
    """Impiegato fisso che percepisce lo stipendio base"""
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)
    
    def get_stipendio(self):
        return self._stipendio
    
    def calcola_stipendio(self):
        return self._stipendio


class ImpiegatoAProvvigione(Impiegato):
    """Impiegato a provvigione che percepisce uno stipendio maggiorato"""
    def __init__(self, nome, cognome, stipendio_base):
        super().__init__(nome, cognome, stipendio_base)
        self._bonus = 0.0 # default a zero

    def set_bonus(self, bonus_vendita): # setter per il bonus
        self._bonus = bonus_vendita
    
    def get_stipendio(self): # getter per lo stipendio 
        return self._stipendio + self._bonus
    
    def calcola_stipendio(self):
        return self._stipendio + self._bonus
    

class Azienda:
    """Azienda gestisce gli impiegati"""
    def __init__(self):
        self.impiegati = []
    
    def aggiungi_impiegato(self, impiegato):
        self.impiegati.append(impiegato)

    def stampa_stipendi(self):
        print("\n--- Elenco Stipendi Impiegati ---")
        for imp in self.impiegati:
            print(f"{imp.nome} {imp.cognome} - Stipendio: {imp.calcola_stipendio():.2f}€")


# Entry point
if __name__ == "__main__":
    # istanzia azienda
    azienda = Azienda() 
    # crea gli impiegati
    imp1 = ImpiegatoFisso("Marco", "Rossi", 2500)
    imp2 = ImpiegatoAProvvigione("Luca", "Basile", 1800)
    imp2.set_bonus(600)
    # li aggiungo all'azienda
    azienda.aggiungi_impiegato(imp1)
    azienda.aggiungi_impiegato(imp2)
    # stampa l'elenco 
    azienda.stampa_stipendi()
