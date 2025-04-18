import numpy as np


class ArrayOperations:
    def __init__(self):
        self.array = None # inizializzato a None

    def create(self, type_arr="lin"):
        """Crea un array: linspace o random"""
        if type_arr == "lin":
            self.array = np.linspace(0, 10, 50)
        elif type_arr == "random":
            self.array = np.random.random(50)
        else:
            raise ValueError("Tipo non supportato. Usa 'lin' o 'random'.")
        print("Array creato:")
        print(self.array)
        return self.array

    def arr_sum(self, arr1, arr2):
        """Somma elemento per elemento due array"""
        if len(arr1) != len(arr2):
            raise ValueError("Gli array devono avere la stessa lunghezza.")
        arr_res = np.array([i + j for i, j in zip(arr1, arr2)])
        sum_ = np.sum(arr_res)
        return f"Array somma: {arr_res}\nSomma totale: {sum_}"

    def filter_sum_elements(self, arr, soglia=5):
        """Somma gli elementi maggiori di una soglia"""
        filtrati = [i for i in arr if i > soglia]
        somma = sum(filtrati)
        return f"Somma degli elementi > {soglia}: {somma}"

            
def menu():
    ops = ArrayOperations()

    while True:
        print("\n--- MENU ---")
        print("1. Crea array (linspace)")
        print("2. Crea array (random)")
        print("3. Somma due array")
        print("4. Somma valori > soglia")
        print("0. Esci")

        scelta = input("Scegli un'opzione: ")

        if scelta == "1":
            ops.create("lin")

        elif scelta == "2":
            ops.create("random")

        elif scelta == "3":
            print("Crea due array prima della somma.")
            arr1 = ops.create("lin")
            arr2 = ops.create("random")
            print(ops.arr_sum(arr1, arr2))

        elif scelta == "4":
            soglia = float(input("Inserisci la soglia: "))
            if ops.array is not None:
                print(ops.filter_sum_elements(ops.array, soglia))
            else:
                print("Errore: devi prima creare un array.")

        elif scelta == "0":
            print("Uscita dal programma.")
            break

        else:
            print("Opzione non valida. Riprova.")


if __name__ == '__main__':
    menu()
        
"""     
class Array:
    
    def __init__(self, linspace, random):
        self.lin = linspace
        self.rand = random
    
    def 
"""