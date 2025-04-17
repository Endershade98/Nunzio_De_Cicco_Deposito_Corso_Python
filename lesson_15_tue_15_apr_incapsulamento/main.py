class Computer:
    
    def __init__(self, nome_proc):
       self.__processore = nome_proc # Attributo privato

    def get_processore(self):
       return self.__processore

    def set_processore(self, processore):
       self.__processore = processore

pc = Computer("Intel i5")
print(pc.get_processore()) 
# Accede all'attributo privato tramite il getter
pc.set_processore("AMD Ryzen 5") 
# Modifica l'attributo privato tramite il setter
print(pc.get_processore())


# Variabile globale
numero = 10

def funzione_esterna():
    # Variabile locale nella funzione esterna
    numero = 5
    print("Numero dentro funzione_esterna (locale):", numero)    

    def funzione_interna():
        # Utilizzo nonlocal per modificare la variabile locale della funzione esterna
        nonlocal numero
        numero = 3
        print("Numero dentro funzione_interna (nonlocal):", numero)
        
    funzione_interna()

print("Numero nel main (globale):", numero)
funzione_esterna()
print("Numero nel main dopo chiamata (globale non cambiato):", numero)