import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Generazione di 30 temperature casuali tra 10°C e 35°C
temperature = np.random.uniform(10, 35, size=30)

# Creazione del DataFrame
df_temperature = pd.DataFrame({'temperature': temperature})

# Crea una serie di date da 1 a 30 aprile 2025
date = pd.date_range(start="2025-04-01", periods=30)

# Crea il DataFrame
df_temperature = pd.DataFrame({
    'data': date,
    'temperature': temperature
})

# Calcoli statistici sulla colonna 'temperature'
temp_max = df_temperature['temperature'].max()
temp_min = df_temperature['temperature'].min()
temp_mean = df_temperature['temperature'].mean()
temp_median = df_temperature['temperature'].median()

# Stampa dei risultati
print(f"Temperatura Massima: {temp_max:.2f} °C")
print(f"Temperatura Minima: {temp_min:.2f} °C")
print(f"Temperatura Media: {temp_mean:.2f} °C")
print(f"Temperatura Mediana: {temp_median:.2f} °C")

# Generazione dell'asse x (giorni del mese)
giorni = range(1, len(df_temperature) + 1)


# Creazione del grafico
plt.figure(figsize=(10, 5))
plt.plot(giorni, df_temperature['temperature'], marker='o', linestyle='-', color='tab:blue')
plt.title("Andamento della Temperatura Giornaliera")
plt.xlabel("Giorno del Mese")
plt.ylabel("Temperatura (°C)")
plt.grid(True)
plt.savefig('test_plot.png')

"""
# Funzione per visualizzare le temperature con linee statistiche
def plot_temperature_with_stats(df, show_max=True, show_min=True, show_mean=True, show_median=True):
    plt.figure(figsize=(12, 6))
    plt.plot(df['temperature'], marker='o', label='Temperature Giornaliera')

    if show_max:
        plt.axhline(df['temperature'].max(), color='red', linestyle='--', label=f'Max ({df["temperature"].max():.1f}°C)')
    if show_min:
        plt.axhline(df['temperature'].min(), color='blue', linestyle='--', label=f'Min ({df["temperature"].min():.1f}°C)')
    if show_mean:
        plt.axhline(df['temperature'].mean(), color='green', linestyle='--', label=f'Media ({df["temperature"].mean():.1f}°C)')
    if show_median:
        plt.axhline(df['temperature'].median(), color='purple', linestyle='--', label=f'Mediana ({df["temperature"].median():.1f}°C)')

    plt.title('Andamento della Temperatura Giornaliera')
    plt.xlabel('Giorno')
    plt.ylabel('Temperatura (°C)')
    plt.legend()
    plt.grid(True)
    plt.savefig('test_plot.png')

# Esempio d'uso
#plot_temperature_with_stats(df, show_max=True, show_min=True, show_mean=True, show_median=True)


class TemperaturePlotter:
    
    def __init__(self):
        self.df
"""