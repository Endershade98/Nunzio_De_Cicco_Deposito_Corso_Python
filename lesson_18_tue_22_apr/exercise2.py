import pandas as pd

file_path = "/home/endershade/Desktop/Python_Course_Repo/vendite_per_citta.csv"
# Carica il file CSV
df = pd.read_csv(file_path)

# Aggiungi colonna "Totale Vendite"
df["Totale Vendite"] = df["Quantità"] * df["Prezzo Unitario"]

# Totale delle vendite per prodotto
vendite_per_prodotto = df.groupby("Prodotto")["Totale Vendite"].sum().reset_index()

# Prodotto più venduto per quantità
prodotto_piu_venduto = df.groupby("Prodotto")["Quantità"].sum().idxmax()

# Città con il maggior volume di vendite totali
citta_maggior_vendite = df.groupby("Città")["Totale Vendite"].sum().idxmax()

# Nuovo DataFrame con vendite superiori a 1000 euro
vendite_over_1000 = df[df["Totale Vendite"] > 1000]

# Ordina il DataFrame originale per "Totale Vendite" in ordine decrescente
df_ordinato = df.sort_values(by="Totale Vendite", ascending=False)

# Numero di vendite per ogni città
conteggio_vendite_per_citta = df["Città"].value_counts()


# STAMPA DEI RISULTATI

print("\nTotale vendite per prodotto:")
print(vendite_per_prodotto)

print("\nProdotto più venduto per quantità:")
print(prodotto_piu_venduto)

print("\nCittà con il maggior volume di vendite totali:")
print(citta_maggior_vendite)

print("\nPrime 5 vendite superiori a 1000€:")
print(vendite_over_1000.head())

print("\nPrime 5 righe ordinate per Totale Vendite:")
print(df_ordinato.head())

print("\nNumero di vendite per ogni città:")
print(conteggio_vendite_per_citta)