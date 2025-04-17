import army_utilities as util


class ControlloMilitare(util.Fanteria, util.Artiglieria, util.Cavalleria, util.SupportoLogistico, util.Ricognizione):
    unità_registrate = {}  # dizionario: nome_unità -> oggetto_unità

    @classmethod
    def registra_unità(cls, unità):
        """Registra le unità in un dizionario"""
        cls.unità_registrate[unità.nome] = unità
        print(f"Unità '{unità.nome}' registrata con successo.")

    @classmethod
    def mostra_unità(cls):
        """Mostra tutte le unità registrate"""
        if not cls.unità_registrate:
            print("Nessuna unità registrata.")
        else:
            print("Unità registrate:")
            for nome in cls.unità_registrate:
                print(f" - {nome}")

    @classmethod
    def dettagli_unità(cls, nome):
        """"""
        unità = cls.unità_registrate.get(nome) # 
        if not unità:
            print(f"Nessuna unità trovata con il nome: {nome}")
            return
        
        print(f"Dettagli dell'unità '{nome}':")
        for attr in vars(unità): # restituisce un dizionario con tutti gli attributi (e i loro valori) di un oggetto, come se stessi facendo obj.__dict__
            print(f" - {attr}: {getattr(unità, attr)}") # permette di ottenere il valore di un attributo, dato il suo nome come stringa
