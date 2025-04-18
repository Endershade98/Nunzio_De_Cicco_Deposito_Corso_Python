class Veicolo:
    """Veicolo rappresenta un veicolo generico ed è la classe Padre"""
    def __init__(self, marca: str, anno: int, targa: str, revisione: bool):
        self._marca = marca
        self._anno = anno
        self._targa = targa
        self._revisione = revisione
    
    # tutti i metodi getter
    def get_marca(self):
        """restituisce la marca"""
        return self._marca

    def get_anno(self):
        """restituisce l'anno"""
        return self._anno

    def get_targa(self):
        """restiruisce la targa"""
        return self._targa

    def get_revisione(self):
        """restiruisce la revisione"""
        return self._revisione

    # tutti i metodi setter
    def set_marca(self, marca: str):
        """setta la marca"""
        self._marca = marca

    def set_anno(self, anno: int):
        """setta l'anno"""
        self._anno = anno

    def set_targa(self, targa: str):
        """setta la targa"""
        self._targa = targa

    def set_revisione(self, revisione: bool):
        """setta la revisione"""
        self._revisione = revisione

    def descrivi(self):
        """fornisce una descrizione del veicolo"""
        return f"Marca: {self._marca}, Anno: {self._anno}, Targa: {self._targa}, Revisione: {self._revisione}"


class Auto(Veicolo):
    """Auto rappresenta un'auto ed eredita dalla classe Veicolo"""
    def __init__(self, marca, anno, targa, revisione, numero_porte):
        super().__init__(marca, anno, targa, revisione)
        self.numero_porte = numero_porte # attributo proprio di Auto

    def descrivi(self):
        base = super().descrivi() #sovrascrivo descrivi()
        return f"{base}, Porte: {self.numero_porte}"


class Moto(Veicolo):
    """Moto rappresenta una moto ed eredita dalla classe Moto"""
    def __init__(self, marca, anno, targa, revisione, tipo_moto):
        super().__init__(marca, anno, targa, revisione)
        self.tipo_moto = tipo_moto # attributo proprio di Moto

    def descrivi(self):
        base = super().descrivi() #sovrascrivo descrivi()
        return f"{base}, Tipo Moto: {self.tipo_moto}"


class Camion(Veicolo):
    """Camion rappresenta un camion ed eredita dalla classe Moto"""
    def __init__(self, marca, anno, targa, revisione, carico_massimo):
        super().__init__(marca, anno, targa, revisione)
        self.carico_massimo = carico_massimo # attributo proprio di Camion

    def descrivi(self):
        base = super().descrivi() #sovrascrivo descrivi()
        return f"{base}, Carico massimo: {self.carico_massimo} kg"


# Metodo polimorfico con parametro un generico veicolo
def mostra_descrizioni(veicoli):
    print("\nDescrizione dei veicoli:")
    for v in veicoli:
        print(v.descrivi()) # chiama descrivi()

# Menu interattivo
def menu_veicoli():
    veicoli = []

    while True:
        print("\n--- MENU VEICOLI ---")
        print("1. Aggiungi Auto")
        print("2. Aggiungi Moto")
        print("3. Aggiungi Camion")
        print("4. Mostra veicoli e esci")
        scelta = input("Scegli un'opzione (1-4): ")

        if scelta in ["1", "2", "3"]:
            marca = input("Marca: ")
            try:
                anno = int(input("Anno di immatricolazione: "))
                targa = input("Targa: ")
                revisione_input = input("Revisione effettuata? (s/n): ").lower()
                if revisione_input not in ['s', 'n']:
                    raise ValueError("Input revisione non valido")
                revisione = revisione_input == 's'
            except ValueError as e:
                print(f"Errore nei dati: {e}")
                continue

            if scelta == "1":
                try:
                    porte = int(input("Numero porte: "))
                    veicoli.append(Auto(marca, anno, targa, revisione, porte))
                except ValueError:
                    print("Inserire un numero valido per le porte.")
            elif scelta == "2":
                tipo = input("Tipo moto (es. Enduro, Scooter): ")
                veicoli.append(Moto(marca, anno, targa, revisione, tipo))
            elif scelta == "3":
                try:
                    carico = float(input("Carico massimo in kg: "))
                    veicoli.append(Camion(marca, anno, targa, revisione, carico))
                except ValueError:
                    print("Inserire un numero valido per il carico.")

        elif scelta == "4":
            break
        else:
            print("Scelta non valida.")

    if veicoli:
        mostra_descrizioni(veicoli)
    else:
        print("Nessun veicolo inserito.")

# Avvio
if __name__ == "__main__":
    menu_veicoli()
