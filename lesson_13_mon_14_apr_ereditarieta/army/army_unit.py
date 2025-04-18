
class UnitaMilitare:

    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati
        self.posizione = "Base" # dove si trova l'unità
        self.stato = "in attesa" # cosa sta facendo l'unità
        self.morale = 100 # il morale dell esercito parte da 100 punti
        self.rifornimenti = 100 # le unità di rifornimento partono da 100 punti

    def muovi(self, destinazione):
        """Muove l'unità verso una destinazione precisa cambia la posizione e lo stato"""
        self.posizione = destinazione
        self.stato = "in marcia"
        return f"{self.nome} si muove verso {destinazione}."

    def attacca(self, obiettivo):
        """Attacca un preciso obiettivo militare cambiando lo stato"""
        self.stato = "in combattimento"
        return f"{self.nome} attacca {obiettivo} con {self.numero_soldati} soldati."

    def ritira(self):
        """Fa rititare l'unita militare cambiando lo stato"""
        self.stato = "ritirata"
        self.morale = max(0, self.morale - 10) # in percentuale
        return f"{self.nome} si ritira. Morale ora: {self.morale}%."

    def stato_attuale(self):
        """restituisce lo stato dell'unità militare"""
        return f"{self.nome} | Soldati: {self.numero_soldati} | Stato: {self.stato} | Posizione: {self.posizione} | Morale: {self.morale}% | Rifornimenti: {self.rifornimenti}%"
