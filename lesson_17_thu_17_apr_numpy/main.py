# metodi principali di numpy


import numpy as np

# Creazione di un array
arr = np.array([1, 2, 3, 4, 5])


# Utilizzo di alcuni metodi
print("Forma dell'array:", arr.shape) # Output: (5,) tupla di numerodi righe=5 e numero colonne=0

print("Dimensioni dell'array:", arr.ndim) # Output: 1

print("Tipo di dati:", arr.dtype) # Output: int64 (varia a seconda della piattaforma)

print("Numero di elementi:", arr.size) # Output: 5

print("Somma degli elementi:", arr.sum()) # Output: 15 operazioni vettoriali (hanno le parentesi tonde, sono propri di numpy)

print("Media degli elementi:", arr.mean()) # Output: 3.0

print("Valore massimo:", arr.max()) # Output: 5

print("Indice del valore massimo:", arr.argmax()) # Output: 4


arr = np.array([1, 2, 3], dtype='int32') # obbliga il tipo a cambiare (non come shape che restituisc il tipo)
print(arr.dtype) # Output: int32


arr = np.arange(10) # crea un array contenente una sequenza di numeri, simile a range di Python
print(arr) # Output: [0 1 2 3 4 5 6 7 8 9]


arr = np.arange(6)
reshaped_arr = arr.reshape((2, 3)) # cambia la forma di un array senza modificarne i dati
print(reshaped_arr)
# Output: [[0 1 2] [3 4 5]]