import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Impostazioni iniziali
np.random.seed(42)
giorni = np.arange(365)
media_base = 2000 # settaggio della media e deviazione standard
deviazione = 500

# 2. Creazione trend e rumore
trend = giorni * 2  # Aumento lineare: +2 visitatori al giorno
rumore = np.random.normal(loc=0, scale=deviazione, size=365)
visitatori = media_base + trend + rumore

# 3. Creazione serie temporale e DataFrame
date = pd.date_range(start="2024-01-01", periods=365)
df = pd.DataFrame({'visitatori': visitatori}, index=date) # date come indice

# 4. Calcolo media e deviazione standard mensile
df_mensile = df['visitatori'].resample('M').agg(['mean', 'std'])

# 5. Calcolo media mobile a 7 giorni
df['media_mobile_7gg'] = df['visitatori'].rolling(window=7).mean()

# 6. Salvataggio dei dati su CSV
df.to_csv("visitatori_parco_2024.csv", index_label='data')
df_mensile.to_csv("visitatori_parco_mensile.csv", index_label='mese')

# 7. Grafico visitatori giornalieri + media mobile
plt.figure(figsize=(14, 6))
plt.plot(df.index, df['visitatori'], label='Visitatori Giornalieri', color='lightblue')
plt.plot(df.index, df['media_mobile_7gg'], label='Media Mobile (7 giorni)', color='blue', linewidth=2)
plt.title("Visitatori Giornalieri con Media Mobile Settimanale")
plt.xlabel("Data")
plt.ylabel("Numero di Visitatori")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 8. Grafico media mensile
plt.figure(figsize=(12, 5))
plt.plot(df_mensile.index, df_mensile['mean'], marker='o', color='darkgreen')
plt.title("Media Mensile dei Visitatori")
plt.xlabel("Mese")
plt.ylabel("Visitatori Medi")
plt.grid(True)
plt.tight_layout()
plt.show()

