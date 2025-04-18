import numpy as np


numbers = np.arange(10, 49)
print(numbers)
print(numbers.dtype)

numbers_float = np.arange(10, 49, dtype='float64')
print(numbers_float)
print(numbers_float.dtype)
print(numbers.shape)


def info(x: np.array):
    a = int(input("Enter an integer number a (10):"))
    b = int(input("Enter an integer number b (49):"))
    arr = np.arange(a, b)
    if arr.dtype == 'int64':
        print(numbers)
        print(numbers.dtype)
    
    
    
arr = np.array([1, 2, 3, 4, 5])

# Indexing
print(arr[0]) # Output: 1

# Slicing
print(arr[1:3]) # Output: [2 3]

# Boolean Indexing
print(arr[arr > 2]) # Output: [3 4 5]


arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12]])

# Slicing sulle righe
print(arr_2d[1:3]) # Output: [[ 5 6 7 8]    dalla riga 1 alla 3 (esclusa)
                           # [ 9 10 11 12]]
# Slicing sulle colonne
print(arr_2d[:, 1:3]) # Output: [[ 2 3]    tutte le righe
                              # [ 6 7]     dalla colonna 1 alla 3 (esclusa)
                              # [10 11]]
# Slicing misto
print(arr_2d[1:, 1:3]) # Output: [[ 6 7]  dalla riga 1 fino alla fine
                               # [10 11]]  dalla colonna 1 alla 3 (esclusa)
                               
    
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing di base
print(arr[2:7]) # Output: [2 3 4 5 6] dall'elemento di indice 2 al 7

# Slicing con passo
print(arr[1:8:2]) # Output: [1 3 5 7] dall'elemento

# Omettere start e stop
print(arr[:5]) # Output: [0 1 2 3 4]
print(arr[5:]) # Output: [5 6 7 8 9]

# Utilizzare indici negativi
print(arr[-5:]) # Output: [5 6 7 8 9]
print(arr[:-5]) # Output: [0 1 2 3 4]


arr = np.array([10, 20, 30, 40, 50])

# Utilizzo di un array di indici
indices = np.array([1, 3])
print(arr[indices]) # Output: [20 40]

# Utilizzo di una lista di indici
indices = [0, 2, 4]
print(arr[indices]) # Output: [10 30 50]


arr = np.linspace(0, 1, 5)
print(arr) # Output: [0. 0.25 0.5 0.75 1. ]


random_arr = np.random.rand(3, 3)
# Matrice 3x3 con valori casuali uniformi tra 0 e 1
print(random_arr)

arr = np.array([1, 2, 3, 4, 5])

sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)

print("Sum:", sum_value) # Output: Sum: 15
print("Mean:", mean_value) # Output: Mean: 3.0
print("Standard Deviation:", std_value)
# Output: Standard Deviation: 1.4142135623730951
