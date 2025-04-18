import numpy as np
import random

print("\n------Esercizio 1-------")

N = int(input("Enter the number N (20): "))
a = int(input("Enter an integer number a (10):"))
b = int(input("Enter an integer number b (50):"))


arr = np.array([random.randint(a, b) for number in range(N)])

print(arr)
# primi 10 elementi
print(arr[:10])
# ultimi 5 elementi
print(arr[50:5:-1])
# dal indice 5 all'indice 15 (escluso)
print(arr[5:15])
# estrarre ogni terzo elemento
print(arr[::3])
# modifica gli elementi dal 5 al 10 con 99
arr[5:10] = 99
print(arr[5:10])


print("\n------Esercizio 2-------")


a = 1
b = 100
N = 6


matrix = np.array([[random.randint(a, b) for rows in range(N)] for columns in range(N)])
print("Matrix:")
print(matrix)

# Sub-matrix con slicing da indici specifici (esempio: righe 1 e 2, colonne 3 e 4)
indexes = ([1, 2, 3, 4], [1, 2, 3, 4])  # tuple di due liste: righe e colonne
sub_matrix = matrix[np.ix_(*indexes)]
print("\nSub-matrix (righe 1-2, colonne 3-4):")
print(sub_matrix)

# Matrice invertita verticalmente (flip verticale)
rev_matrix = matrix[::-1]
print("\nReversed matrix:")
print(rev_matrix)

# Diagonale della matrice invertita
diag = np.array([rev_matrix[i][i] for i in range(N)])
print("\nDiagonale della matrice invertita:")
print(diag)

# Crea un filtro per selezionare solo colonne con indice %3==0
columns_to_keep = [x for x in range(N) if x % 3 == 0]
filt_matrix = rev_matrix[:, columns_to_keep]
print("\nFiltered matrix (solo colonne con indice %3==0):")
print(filt_matrix)


while True:
    start = int(input("Enter start: "))
    stop = int(input("Enter stop: "))
    step = int(input("Enter step: "))
   