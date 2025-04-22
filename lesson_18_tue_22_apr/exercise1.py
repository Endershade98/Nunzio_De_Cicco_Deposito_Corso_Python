import pandas as pd


# Percorso del file CSV
file_path = 'lesson_18_tue_22_apr/persons_data.csv'

# Caricamento dei dati nel DataFrame
df = pd.read_csv(file_path)

#le prime 5 e le ultime righe (default 5 rows) del DataFrame
print(df.head())
print(df.tail())

# Visualizzare il type colonna per colonna
for column in df[::]:
    for data in df[column]:
        print(type(data))


# Converti colonne numeriche con errori (come spazi o 'abc') in numeri
df['Età'] = pd.to_numeric(df['Età'], errors='coerce')
df['Salario'] = pd.to_numeric(df['Salario'], errors='coerce')

# Sostituire i valori Nan con la mediana
# Calcola la mediana della colonna
mediana_eta = df['Età'].median()
mediana_salario = df['Salario'].median()
# Sostituisci i valori mancanti con la mediana
df['Età'].fillna(mediana_eta, inplace=True)
# Calcoli statistici per colonna
print("Media per colonna:")
print(df.mean(numeric_only=True))

print("\nMediana per colonna:")
print(df.median(numeric_only=True))

print("\nDeviazione standard per colonna:")
print(df.std(numeric_only=True))

# Aggiunta nuove colonne 
df['Categoria Età'] = 'Sconosciuto'

# Assegna i valori in base all'intervallo di età con boolean conditions
# df.loc[condizione, 'colonna'] = valore modifica solo le righe che soddisfano la condizione.
df.loc[df['Età'] <= 18, 'Categoria Età'] = 'Giovane'
df.loc[(df['Età'] > 18) & (df['Età'] <= 65), 'Categoria Età'] = 'Adulto'
df.loc[df['Età'] > 65, 'Categoria Età'] = 'Senior'

# Salva il DataFrame in un nuovo file CSV
df.to_csv('persone_pulite.csv', index=False)