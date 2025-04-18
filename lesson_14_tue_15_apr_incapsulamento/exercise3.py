# polimorfismo 

class Animale:
    def emetti_suono(self):
        print("Questo animale fa un suono")

class Cane(Animale): #esempio di polimorfismo attivo sfruttando l'ereditarietà
    def emetti_suono(self):
        print("Bau")

class Gatto(Animale):
    def emetti_suono(self):
        print("Miao")


# esempio di Duck typing polimorfismo forte
def fai_parlare(animale):
    # Non importa di che tipo sia l'animale,
    print(animale.emetti_suono())


print(Animale().emetti_suono())
print(fai_parlare(Cane()))


# esempio di overloading
class Stampa:
    def mostra(self, a=None, b=None):
        if a is not None and b is not None:
            print(a + b)
        elif a is not None:
            print(a)
        else:
            print("Niente da mostrare")
            
print(Stampa().mostra(3, 6))



class Cane:
    def parla(): #polimorfismo passivo i due metodi funzionano allo stesso modo
        print("Bau!")
        
class Gatto:
    def parla(): 
        print("Miao!")
        

print(Cane().parla())
print(Gatto().parla())
        
