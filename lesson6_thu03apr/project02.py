def verifica(func):
    
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} è in esecuzione")
        risultato = func(**args, **kwargs)
        print(f"{func.__name__} è stata eseguita")
        return risultato
    return wrapper


class Ristorante:
    
    def __init__(self, nome_ristorante: str, tipo_cucina: str) -> None:
        self.nome = nome_ristorante
        self.tipo = tipo_cucina
        self.aperto = False
        self.menu = {}
        
    @verifica    
    def descrivi_ristorante(self):
        """stampa la descrizione del ristorante"""
        description = f"Il ristorante {self.nome} propone la sua tipica cucina {self.tipo}"
        return description
    
    @verifica    
    def stato_apertura(self):
        """stampa lo stato di apertura del ristorante"""
        return self.aperto
    
    @verifica    
    def chiudi_ristorante(self):
        """chiude il ristorante cambindo lo stato di apertura"""
        if self.aperto == True:
            self.aperto = False
            return self.aperto
        else:
            return self.aperto
    
    @verifica    
    def apri_ristorante(self):
        """apre il ristorante cambindo lo stato di apertura"""
        if self.aperto == False:
            self.aperto = True
            return self.aperto
        else:
            return self.aperto
    
    @verifica    
    def aggiungi_al_menu(self, nuovo_piatto: str, prezzo: float):
        """aggiunge un nuovo piatto al menu col prezzo"""
        self.menu[nuovo_piatto] = prezzo
        return f"{nuovo_piatto} è atato aggiunto al menù"
        
    @verifica    
    def togli_dal_menu(self, piatto_da_eliminare):
        """togli dal menu un piatto"""
        del self.menu[piatto_da_eliminare]
        return f"{piatto_da_eliminare} è stato eliminato"
    
    @verifica    
    def stampa_menu(self):
        """stampa il menu aggiornato"""
        for chiave, valore in self.menu.items():
            print(f"{chiave}: {valore}")

