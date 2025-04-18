from abc import ABC, abstractmethod


class Forma:
    """rappresenta una generica forma geometrica"""
    @abstractmethod
    def area(self):
        """calcola l'area della forma"""
        pass
    
    @abstractmethod
    def perimetro(self):
        """calcola il perimetro della forma"""
        pass
    
# Cerchio, Rettangolo, Triangolo
class Cerchio(Forma):
    """rappresenta un cerchio"""
    def __init__(self, raggio):
        self.raggio = raggio
        self.pi = 3.14
        
    def area(self):
        return self.pi*(self.raggio)**2
    
    def perimetro(self):
        return 2*self.pi*self.raggio

class Rettangolo(Forma):
    """rapresenta un rettangolo"""
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
        
    def area(self):
        return self.base*self.altezza
    
    def perimetro(self):
        return 2*(self.base+self.altezza)
    

class Triangolo(Forma):
    """rappresenta un triangolo"""
    def __init__(self, base, altezza):
        self.base = base
        self.altezza = altezza
        
    def area(self):
        return (self.base*self.altezza)/2
    
    def perimetro(self):
        lato_obliquo = ((self.base / 2) ** 2 + self.altezza ** 2)**0.5
        res = self.base + 2 * lato_obliquo
        return res
        
# Funzione polimorfica per trovare la forma con area o perimetro maggiore
def confronta_forme(forme):
    if not forme:
        print("Nessuna forma da confrontare.")
        
    # clacolo dei masimmi valori di perimetro e area utilizzando la lambda function
    forma_area_max = max(forme, key=lambda f: f.area())
    forma_perimetro_max = max(forme, key=lambda f: f.perimetro())

    print("\nForma con area maggiore:")
    print(forma_area_max)
    print("\nForma con perimetro maggiore:")
    print(forma_perimetro_max)

# Lista per salvare le forme
forme = []

# Menu 
def menu():
    # il menu è avviato finche non salva 4 forme
    while len(forme) < 4:
        print("\n--- MENU FORME GEOMETRICHE ---")
        print("1. Aggiungi Cerchio")
        print("2. Aggiungi Rettangolo")
        print("3. Aggiungi Triangolo (isoscele)")
        print("4. Esci e confronta forme")
        scelta = input("Scegli un'opzione (1-4): ")

        if scelta == "1":
            r = float(input("Inserisci il raggio del cerchio: "))
            forme.append(Cerchio(r))
        elif scelta == "2":
            b = float(input("Base del rettangolo: "))
            h = float(input("Altezza del rettangolo: "))
            forme.append(Rettangolo(b, h))
        elif scelta == "3":
            b = float(input("Base del triangolo isoscele: "))
            h = float(input("Altezza del triangolo: "))
            forme.append(Triangolo(b, h))
        elif scelta == "4":
            break
        else:
            print("Scelta non valida, riprova.")

    # Visualizza le forme inserite
    print("\nElenco delle forme inserite:")
    for f in forme:
        print(f)

    confronta_forme(forme)

# Entry Point
if __name__ == "__main__":
    menu()