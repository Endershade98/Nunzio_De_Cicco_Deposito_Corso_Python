def check(func):
    
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} è in esecuzione")
        risultato = func(**args, **kwargs)
        print(f"{func.__name__} è stata eseguita")
        return risultato
    return wrapper


class Restaurant:
    
    def __init__(self, name: str, food_type: str, status=False) -> None:
        self.name = name
        self.type = food_type
        self.status = status
        self.menu = {}
        
    @check    
    def describe(self):
        """stampa la descrizione del ristorante"""
        return f"The restaurant {self.name}has this type of food{self.food_type}"
     
    @check    
    def add_to_menu(self, nuovo_piatto: str, prezzo: float):
        """aggiunge un nuovo piatto al menu col prezzo"""
        self.menu[nuovo_piatto] = prezzo
        return f"{nuovo_piatto} è atato aggiunto al menù"
        
    @check    
    def remove_from_menu(self, piatto_da_eliminare):
        """togli dal menu un piatto"""
        del self.menu[piatto_da_eliminare]
        return f"{piatto_da_eliminare} è stato eliminato"
    
    @check    
    def show_menu(self):
        """stampa il menu aggiornato"""
        for chiave, valore in self.menu.items():
            print(f"{chiave}: {valore}")

    @check    
    def show_status(self):
        """stampa lo stato di apertura del ristorante"""
        return self.aperto
    
    @check    
    def close_restaurant(self):
        """chiude il ristorante cambindo lo stato di apertura"""
        if self.aperto == True:
            self.aperto = False
            return self.aperto
        else:
            return self.aperto
    
    @check    
    def open_restaurant(self):
        """apre il ristorante cambindo lo stato di apertura"""
        if self.aperto == False:
            self.aperto = True
            return self.aperto
        else:
            return self.aperto
    
    
