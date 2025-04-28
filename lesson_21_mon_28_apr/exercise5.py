import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carica il dataset (modifica questo passaggio in base alla tua fonte dati)
df = pd.read_csv('path_to_your_dataset.csv')  # Sostituisci con il percorso del tuo dataset

# Seleziona solo le colonne numeriche
df_numeric = df.select_dtypes(include=['number'])

# Calcola la matrice di correlazione
correlation_matrix = df_numeric.corr()

# Visualizza la matrice di correlazione usando una heatmap
plt.figure(figsize=(10, 8))  # Imposta la dimensione della figura
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Matrice di Correlazione delle Feature Numeriche")
plt.show()
