
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


plt.rcParams['figure.figsize'] = [10, 6]  
# Imposta la dimensione predefinita delle figure

plt.rcParams['figure.dpi'] = 100          
# Imposta la risoluzione delle figure in DPI

# Configura Seaborn
sns.set_theme(style="darkgrid")

# Crea alcuni dati
data = np.random.normal(size=100)

# Crea un grafico
sns.histplot(data, kde=True)
plt.title('Distribuzione dei dati')
plt.savefig("curva_roc.png")


x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]


plt.figure()
plt.plot(x, y)
plt.title('Grafico a Linee')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.savefig("grafico_a_linee.png")


categories = ['A', 'B', 'C', 'D', 'E']
values = [3, 7, 2, 5, 8]

plt.figure()
plt.bar(categories, values)
plt.title('Grafico a Barre')
plt.xlabel('Categorie')
plt.ylabel('Valori')
plt.savefig("grafico_a_barre.png")


data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30)
plt.title('Istogramma')
plt.xlabel('Valori')
plt.ylabel('Frequenza')
plt.savefig("istogramma.png")


x = np.random.rand(50)
y = np.random.rand(50)

plt.figure()
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.savefig("scatter_plot.png")