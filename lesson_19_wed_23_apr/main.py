import pandas as pd
import matplotlib.pyplot as plt

# Creazione di un DataFrame da un dizionario
data = {
    'nome': ['Alice','Bob'],
    'età': [25, 30]
    }

df = pd.DataFrame(data)
# Caricamento di un DataFrame da un file CSV
df_csv = pd.read_csv('/home/endershade/Desktop/Python_Course_Repo/lesson_19_wed_23_apr/data.csv')

# Visualizzazione delle statistiche descrittive
print(df.describe())

# Rimozione dei valori mancanti
df_clean = df.dropna()

# Selezione di una colonna
ages = df['età']

# Filtraggio basato su una condizione
adults = df[df['età'] >= 18]

# Ordinamento dei dati per età
df_sorted = df.sort_values(by='età')

# Unione di due DataFrame
merged_df = pd.merge(df, df_csv, on='nome')

# Applicazione di una funzione a una colonna
df['età_doppia'] = df['età'].apply(lambda x: x * 2)

# Esportazione di un DataFrame in un file CSV
df.to_csv('data_output.csv')

# Generazione di una serie di date
date_range = pd.date_range(start='2021-01-01', periods=10, freq='M')

# Resampling dei dati di una serie temporale
df_resampled = df.resample('M').mean()


# Visualizzazione di un grafico a barre delle età
df['età'].plot(kind='bar')
plt.show()
