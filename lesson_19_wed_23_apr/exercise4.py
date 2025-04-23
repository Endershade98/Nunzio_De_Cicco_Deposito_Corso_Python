import pandas as pd

# Caricamento del dataset originale
df = pd.read_csv("dataset_altezza_peso_eta.csv")

# Normalizzazione Min-Max di Altezza e Peso
df_normalized = df.copy()
for col in ['Altezza', 'Peso']:
    min_val = df[col].min()
    max_val = df[col].max()
    df_normalized[col] = (df[col] - min_val) / (max_val - min_val)

# Stampa dei due DataFrame
print("DataFrame originale:\n")
print(df.head())

print("\nDataFrame normalizzato (Min-Max su Altezza e Peso):\n")
print(df_normalized.head())
