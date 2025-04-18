import numpy as np

# creazione dell'array 4x4 con numeri interi casuali tra 10 e 50
matrice = np.random.randint(10, 51, size=(4, 4))
print("Matrice 4x4:")
print(matrice)

# seleziona degli elementi agli indici specificati
righe = [0, 1, 2, 3]
colonne = [1, 3, 2, 0]
selezionati = matrice[righe, colonne]
print("Elementi selezionati (fancy indexing):")
print(selezionati)

# seleziona tutte le righe dispari (indice 1 e 3)
righe_dispari = matrice[1::2]
print("Righe dispari dell'array:")
print(righe_dispari)

# modifica degli elementi selezionati precedentemente aggiungendo 10
matrice[righe, colonne] += 10
print("Matrice dopo modifica degli elementi selezionati:")
print(matrice)


