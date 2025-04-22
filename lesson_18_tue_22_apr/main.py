import pandas as pd

# Percorso del file CSV
file_path = '/home/endershade/Desktop/Python_Course_Repo/lesson_18_tue_22_apr/vendite.csv'

# Caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)

#le prime righe del DataFrame per confermare
print(df.head())
