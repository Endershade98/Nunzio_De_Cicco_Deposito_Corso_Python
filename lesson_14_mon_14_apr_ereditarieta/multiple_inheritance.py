class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
    def mostra_informazioni(self):
        return f"Veicolo di marca: {self.marca}, modello: {self.modello}"


class DotazioniVeicolo:
    
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni
    
    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")


class AutomobileSportiva(Veicolo, DotazioniVeicolo):
    
    def __init__(self, marca, modello, dotazioni, cavalli):
        # eredita da veicolo
        Veicolo.__init__(self, marca, modello)
        #eredita da dotazioni veicolo
        DotazioniVeicolo.__init__(self, dotazioni)
        #aggiunge l'attibuto cavalli proprio di automobile sportiva
        self.cavalli = cavalli
    
    def mostra_informazioni(self):
        # sovrascrittura con super()
        super().mostra_informazioni()
        print(f"Potenza{self.cavalli} CV")
        return self.mostra_dotazioni
    
    

auto_sportiva = AutomobileSportiva("Ferrari", "F8", ["ABS", "Controllo trazione", "Airbag laterali"], 720)

auto_sportiva.mostra_informazioni()