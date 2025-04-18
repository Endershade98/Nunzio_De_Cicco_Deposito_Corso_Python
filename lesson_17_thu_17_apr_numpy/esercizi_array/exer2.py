import numpy as np

# crea la matrice 5x5
matrice = np.arange(1, 26).reshape((5, 5))
print("Matrice 5x5:")
print(matrice)

# estrae la seconda colonna (indice 1)
seconda_colonna = matrice[:, 1]
print("\nSeconda colonna:")
print(seconda_colonna)

# estrae la terza riga (indice 2)
terza_riga = matrice[2, :]
print("\nTerza riga:")
print(terza_riga)

# calcola la somma degli elementi della diagonale principale
somma_diagonale = np.trace(matrice)
print("\nSomma della diagonale principale:")
print(somma_diagonale)


class MatrixManager:
    
    def __init__(self):
        self.matrice = None
        
    def create_matrix(self, start, stop, row, column):
        if self.matrice == None:
            self.matrice = np.arange(start, stop).reshape((row, column))
            print("Matrice 5x5 creata:")
            return self.matrice
        else:
            print("Errore nella creazione della matrice") 
        
    
    def extraxt_column(self, column=1):
        if self.matrice != None:
            seconda_colonna = self.matrice[:, column]
            print("Colonna selezionata (seconda di default):")
            return seconda_colonna
        else:
            print("Errore nell'estrrazione della colonna") 
    
    def extract_row(self, row=2):
        if self.matrice != None:
            terza_riga = self.matrice[row, :]
            print("Riga selezionata (terza di default):")
            return terza_riga
        else:
            print("Errore nell'estrazione della riga") 
    
    def caculate_sum(self):
        if self.matrice != None:
            somma_diagonale = np.trace(self.matrice)
            print("Somma della diagonale principale:")
            return somma_diagonale
        else:
            print("Errore nella somma")
    
    
def menu():
    manager = MatrixManager() # istanza del manager
    
    #while True:
        