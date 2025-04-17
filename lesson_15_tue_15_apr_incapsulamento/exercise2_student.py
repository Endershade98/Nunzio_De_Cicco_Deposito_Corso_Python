
def valida_nome(func):
    
    def wrapper(*args, **kwargs):
        if type(args[0]) == str:
            raise TypeError("Il primo argomento deve essere di tipo stringa (str).")
        return func(*args, **kwargs)
    return wrapper


def valida_eta(func):
    
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise TypeError("Il primo argomento deve essere di tipo stringa (str).")
        return func(*args, **kwargs)
    return wrapper


def valida_voto(func):
    def wrapper(*args, **kwargs):
        if not (0 <= args[0] <= 30):
            raise ValueError("Il voto deve essere compreso tra 0 e 30.")
        return func(*args, **kwargs)
    return wrapper


def ripeti(n):
    def wrapper(func):
        def _wrapper(*args, **kwargs):
            risultati = []
            for _ in range(n):
                risultato = func(*args, **kwargs)
                risultati.append(risultato)
            return risultati  
        return _wrapper
    return wrapper


class Persona:
    
    def __init__(self, nome: str, eta: int) -> None:
        self.__nome = nome
        self.__eta = eta
        
    def presentazione(self):
        return f"Salve sono {self.get_nome()} di {self.get_eta()} anni"
    
    @valida_nome
    def set_nome(self, nuovo_nome):
        if nuovo_nome != " ":
            self.__nome = nuovo_nome
    
    @valida_eta
    def set_eta(self, nuova_eta):
        if nuova_eta >= 18:
            self.__eta = nuova_eta
    
    def get_nome(self):
        return self.__nome
    
    def get_eta(self):
        return self.__eta


class Studente(Persona):
    
    def __init__(self, nome, eta):
        super().__init__(nome, eta)
        self.voti = []
        
    def media(self):
        return sum(self.voti)/len(self.voti) if self.voti else 0
    
    @ripeti(3)
    def aggiungi_voto(self, voto):
            self.voti.append(voto)
    
    def presentazione(self):
        super().presentazione()
        return f"Lo studente {self.get_nome()} di {self.get_eta()} anni ha una media di {self.media():.2f}"
    

class Professore(Persona):
    
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.materia = materia
    
    def  presentazione(self):
        super().presentazione()
        return f"Il professore {self.get_nome()} di {self.get_eta()} anni insegna {self.materia}"
    
    
    
def main():
    studente = Studente("Max", 23)
    print(studente.aggiungi_voto(25))  # viene aggiunto 3 volte
    print(studente.presentazione())


if __name__ == "__main__":
    print("main")
    main()
else:
    print("import")