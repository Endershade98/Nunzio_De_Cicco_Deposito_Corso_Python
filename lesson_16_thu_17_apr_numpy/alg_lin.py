import numpy as np


# Creazione di una matrice quadrata
A = np.array([[1, 2], [3, 4]])
print(A)
# Calcolo dell'inversa della matrice
A_inv = np.linalg.inv(A)
print("Inversa di A:\n", A_inv)
det_A = np.linalg.det(A)
print("\nil determinante di A è: ", det_A)

# Creazione di un vettore
v = np.array([3, 4])

# Calcolo della norma del vettore
norm_v = np.linalg.norm(v)
print("Norma di v:", norm_v) # Output: 5.0

arr = np.array([1, 2, 3, 4])
scalar = 10

# Broadcasting aggiunge lo scalare a ogni elemento dell'array
result = arr + scalar
print(result) # Output: [11 12 13 14]


# Creazione di un array
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Operazioni aritmetiche
c = a + b # Output: [5, 7, 9]

# Funzioni matematiche
d = np.sin(a) # Output: [sin(1), sin(2), sin(3)]

# Algebra lineare
e = np.dot(a, b) # Prodotto scalare: 32

# Broadcasting
f = a + 10 # Output: [11, 12, 13]

