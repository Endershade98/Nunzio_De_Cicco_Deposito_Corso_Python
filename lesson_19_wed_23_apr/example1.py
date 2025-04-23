import pandas as pd
import matplotlib.pyplot as plt

# Creazione di un DataFrame da un dizionario
data = {
    'nome': ['Alice','Bob'],
    'età': [25, 30]
    }

df = pd.DataFrame(data)
print(df)

# Converte in un nuovo formato (csv, jsno o excell)
df.to_csv('data_output.csv')
df.to_json('data_json.json')

# Generazione di una serie di date
date_range = pd.date_range(start='2021-01-01', periods=10, freq='M')
# Resampling dei dati di una serie temporale
df_resampled = df.resample('M').mean()