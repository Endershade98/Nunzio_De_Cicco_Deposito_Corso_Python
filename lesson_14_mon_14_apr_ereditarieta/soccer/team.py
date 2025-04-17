import member_blueprint as mb
import random 


class Giocatore(mb.MembroSquadra):
    
    def __init__(self, name, age, ruolo, numero_maglia):
        super().__init__(name, age)
        self.ruolo = ruolo
        self.numero = numero_maglia
        
    def gioca_partita(self):
        return f"{self.__class__.__name__} gioca nel ruolo di {self.ruolo} col numero {self.numero}"
    
class Allenatore(mb.MembroSquadra):
    
    def __init__(self, name, age, anni_di_esperienza):
        super().__init__(name, age)
        self.anni = anni_di_esperienza
    
    def dirige_allenamento(self):
        return f"{self.name} ha {self.age} anni ed allena da {self.anni} anni"
    
        
class Assistente(mb.MembroSquadra):
    
    def __init__(self, name, age, mansione):
        super().__init__(name, age)
        self.mansione = mansione
    
    def supporta_team(self):
        return f"{self.name} ha la mansione di {self.mansione}"
    
    
class Squadra:
    def __init__(self, nome):
        self.nome = nome
        self.giocatori = []
        self.allenatore = None
        self.assistenti = []
        self.goal = 0
    
    def aggiungi_giocatore(self, giocatore):
        self.giocatori.append(giocatore)
    
    def assegna_allenatore(self, allenatore):
        self.allenatore = allenatore
    
    def aggiungi_assistente(self, assistente):
        self.assistenti.append(assistente)
    
    def segna_goal(self):
        self.goal += random.randint(0, 3)
    
    def stampa_formazione(self):
        print(f"\nFormazione di {self.nome}:")
        for g in self.giocatori:
            print(f" - {g.name} (#{g.numero}, {g.ruolo})")
        if self.allenatore:
            print(f"Allenatore: {self.allenatore.name}")
        for a in self.assistenti:
            print(f"Assistente: {a.name} ({a.mansione})")
