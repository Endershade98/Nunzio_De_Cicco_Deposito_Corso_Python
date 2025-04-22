import pandas as pd
# Creazione di un DataFrame da un dizionario
data = {
    'nome': ['Alice','Bob'],
    'età': [25, 30]
    }

df = pd.DataFrame(data)
# Caricamento di un DataFrame da un file CSV
df_csv = pd.read_csv('data.csv')

# Visualizzazione delle statistiche descrittive
print(df.describe())
# Rimozione dei valori mancanti
df_clean = df.dropna()
