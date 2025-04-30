import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
import matplotlib.pyplot as plt


class VIFCalculator:
    def __init__(self, X):
        """
        X: pandas DataFrame contenente solo le feature numeriche indipendenti.
        """
        self.X = X.copy()
        self.vif_data = None

    def compute_vif(self):
        """
        Calcola il VIF per ogni variabile del DataFrame.
        """
        X_const = add_constant(self.X)
        vif = [
            variance_inflation_factor(X_const.values, i)
            for i in range(1, X_const.shape[1])
        ]
        self.vif_data = pd.DataFrame({
            'feature': self.X.columns,
            'VIF': vif
        })
        return self.vif_data

    def filter_high_vif(self, threshold=5.0):
        """
        Restituisce le feature con VIF superiore alla soglia.
        """
        if self.vif_data is None:
            self.compute_vif()
        return self.vif_data[self.vif_data['VIF'] > threshold]

    def reduce_multicollinearity(self, threshold=5.0, verbose=True):
        """
        Rimuove iterativamente le variabili con VIF superiore alla soglia specificata.
        Restituisce il DataFrame ridotto.
        """
        while True:
            vif_df = self.compute_vif()
            max_vif = vif_df['VIF'].max()
            if max_vif > threshold:
                feature_to_remove = vif_df.loc[vif_df['VIF'].idxmax(), 'feature']
                if verbose:
                    print(f"Rimuovendo '{feature_to_remove}' con VIF={max_vif:.2f}")
                self.X.drop(columns=[feature_to_remove], inplace=True)
            else:
                break
        return self.X.copy()

    def plot_vif(self):
        """
        Visualizza un grafico a barre del VIF.
        """
        if self.vif_data is None:
            self.compute_vif()
        self.vif_data.sort_values('VIF', ascending=False).plot(
            kind='bar', x='feature', y='VIF', legend=False, figsize=(10, 5))
        plt.axhline(y=5, color='r', linestyle='--', label='Soglia VIF = 5')
        plt.title("VIF per variabile")
        plt.ylabel("VIF")
        plt.tight_layout()
        plt.show()

"""
        USE CASE
# Supponi che 'X' sia un DataFrame con solo le variabili indipendenti numeriche
vif_calc = VIFCalculator(X)
X_cleaned = vif_calc.reduce_multicollinearity(threshold=5.0)

# Mostra le nuove feature rimaste
print("Feature rimanenti:", list(X_cleaned.columns))

"""