from data_info import df
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


new_df = df.dropna()# Drop rows with any null values
print("DataFrame senza valori nulli:")
print(new_df)
new_df.fillna(0, inplace=True) # Fill null values with 0


def show_menu():
    """
    Mostra il menu delle opzioni per la gestione dei valori nulli.
    """
    print("Gestione dei valori nulli:")
    print("1. Rimuovi righe con valori nulli")
    print("2. Sostituisci valori nulli con 0")
    print("3. Sostituisci valori nulli con la media della colonna")
    print("4. Sostituisci valori nulli con la mediana della colonna")
    print("5. Sostituisci valori nulli con il valore più frequente della colonna")
    print("6. Sostituisci valori nulli con un valore specifico")
    print("7. Non fare nulla")


def handle_missing_values(df: pd.DataFrame, method: int, value=None):
    """
    Gestisce i valori nulli nel DataFrame in base al metodo scelto.
    
    Args:
        df (pd.DataFrame): Il DataFrame da elaborare.
        method (int): Il metodo di gestione dei valori nulli.
        value: Valore specifico per la sostituzione (se necessario).
    
    Returns:
        pd.DataFrame: Il DataFrame elaborato.
    """
    if method == 1:
        return df.dropna()# Drop rows with any null values
    elif method == 2:
        return df.fillna(0)# Fill null values with 0
    elif method == 3:
        return df.fillna(df.mean())# Fill null values with the mean of the column
    elif method == 4:
        return df.fillna(df.median())# Fill null values with the median of the column
    elif method == 5:
        return df.fillna(df.mode().iloc[0])# Fill null values with the mode of the column
    elif method == 6 and value is not None:
        return df.fillna(value)# Fill null values with a specific value
    else:
        return df

# Esempio di utilizzo
def main():
    
    show_menu()
    choice = int(input("Scegli un'opzione (1-7): "))
    if choice == 1:
        new_df = handle_missing_values(df, 1)
    elif choice == 2:
        new_df = handle_missing_values(df, 2)
    elif choice == 3:
        new_df = handle_missing_values(df, 3)
    elif choice == 4:
        new_df = handle_missing_values(df, 4)
    elif choice == 5:
        new_df = handle_missing_values(df, 5)
    elif choice == 6:
        value = input("Inserisci il valore specifico per la sostituzione: ")
        new_df = handle_missing_values(df, 6, value)
    elif choice == 7:
        new_df = df
    else:
        print("Opzione non valida. Nessuna modifica apportata.")
    print("DataFrame dopo la gestione dei valori nulli:")
    print(new_df)
