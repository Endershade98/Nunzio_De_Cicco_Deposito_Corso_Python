import pandas as pd

# Carica il dataset
file_path = '/home/endershade/Desktop/Python_Course_Repo/summary_machine_learning/data_cleaning_tutorial/example_data.csv'  # Sostituisci con il percorso del tuo file


# Funzione per caricare il dataset
def load_data(file_path):
    """
    Carica il dataset da un file CSV.
    
    Args:
        file_path (str): Il percorso del file CSV.
    
    Returns:
        pd.DataFrame: Il DataFrame caricato.
    """
    return pd.read_csv(file_path)


# Funzione per analizzare il dataset
def analyze_data(data: pd.DataFrame):
    """
    Analizza il dataset e restituisce informazioni utili.
    
    Args:
        data (pd.DataFrame): Il DataFrame da analizzare.
    
    Returns: 
        str:  Statistiche descrittive del dataframe.
    """
    for col in data.columns:
        print(f"\nAnalisi della colonna: {col}")
        print(f"Colonna: {col}")
        print(f"Tipo di dati: {data[col].dtype}")
        print(f"Numero di valori: {data[col].count()}")
        print(f"Numero di valori unici: {data[col].nunique()}")
        print(f"Valore più frequente: {data[col].mode()[0]}")
        print(f"Valore meno frequente: {data[col].value_counts().idxmin()}")
        print(f"Valori unici: {data[col].unique()}")
        print(f"Valori nulli: {data[col].isnull().sum()}")
        print(f"Statistiche descrittive:\n{data[col].describe()}\n")
        

df = load_data(file_path)
analyze_data(df)