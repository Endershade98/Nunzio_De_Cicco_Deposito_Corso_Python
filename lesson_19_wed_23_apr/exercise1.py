import numpy as np
import pandas as pd

# Per risultati ripetibili
np.random.seed(42)
# Quantità di dati
n = 3

# Dati fittizi per "Data","Città","Prodotto" e "Vendite"
date = pd.to_datetime(np.random.choice(pd.date_range('2025-04-01', '2025-04-30'), n))
prodotti = np.random.choice(['Laptop', 'Smartphone', 'Monitor', 'Mouse', 'Tastiera', 'Cuffie', 'Webcam'],size=n)
vendite = np.random.randint(100, 1000+1, n)
città = np.random.choice(['Roma', 'Milano', 'Torino', 'Bologna'], n)

# Costruzione del DataFrame
df = pd.DataFrame({
    'Prodotto': prodotti,
    'Date': date,
    'Vendite': np.round(vendite, 2),
    'Città': città
})

# Stampa di anteprima
print(df.head())

# Salvataggio opzionale in CSV
df.to_csv('dati_casuali.csv', index=False)

# Creazione della tabella pivot media vendite per prodotto
pd.pivot_table(df,                         # Dataframe di riferimento
               values='Vendite',           # Colonna co i dati numerici
               index='Prodotto',           # Colonna da usare come indice
               columns='Città',            # colonne da usare come intestazioni (colonne)
               aggfunc='mean'
               )



