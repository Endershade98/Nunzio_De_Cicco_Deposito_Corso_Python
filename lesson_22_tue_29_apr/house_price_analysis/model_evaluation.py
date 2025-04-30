# import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
# from statsmodels.stats.outliers_influence import variance_inflation_factor
# from statsmodels.tools.tools import add_constant


class ModelEvaluator:
    def __init__(self, X_train, X_test, y_train, y_test, df_full):
        """Inizializzazione della classe con i set di training/test e il DataFrame completo"""
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.df = df_full  # Usato per grafici e analisi esplorativa
        self.results = {}  # Dizionario per salvare i risultati delle metriche
        self.best_model = None  # Conterrà il miglior modello da GridSearchCV
        self.linear_model = None  # Conterrà l'istanza di LinearRegression addestrata

    def run_grid_search(self, model, param_grid, model_name='model'):
        """Esegue una Grid Search con validazione incrociata (5-fold) sul modello specificato"""
        grid_search = GridSearchCV(model, param_grid, cv=5, scoring='r2')
        grid_search.fit(self.X_train, self.y_train)

        # Salva il miglior modello trovato
        self.best_model = grid_search.best_estimator_

        # Valuta il modello sul set di test
        y_pred = self.best_model.predict(self.X_test)

        """Registra le metriche di performance e i parametri ottimali"""
        self.results[f'{model_name}_r2'] = r2_score(self.y_test, y_pred)
        self.results[f'{model_name}_mse'] = mean_squared_error(self.y_test, y_pred)
        self.results[f'{model_name}_params'] = grid_search.best_params_

    def train_linear_regression(self):
        """Crea e addestra un modello di regressione lineare"""
        self.linear_model = LinearRegression()
        self.linear_model.fit(self.X_train, self.y_train)

    def evaluate_linear_regression(self):
        """Verifica che il modello sia stato addestrato"""
        if self.linear_model is None:
            raise ValueError("Il modello lineare non è stato addestrato.")

        # Predice e calcola le metriche sul set di test
        y_pred = self.linear_model.predict(self.X_test)
        self.results['linear_r2'] = r2_score(self.y_test, y_pred)
        self.results['linear_mse'] = mean_squared_error(self.y_test, y_pred)

    def plot_boxplots(self, columns=None):
        """Crea boxplot per le feature specificate o tutte se 'columns' è None"""
        data = self.df if columns is None else self.df[columns]
        plt.figure(figsize=(20, 10))
        data.boxplot(rot=90)
        plt.title('Boxplot delle Feature')
        plt.xticks(rotation=45)
        plt.show()

    def save_results(self, path='results.json'):
        """Esporta i risultati raccolti in un file JSON"""
        import json
        with open(path, 'w') as f:
            json.dump(self.results, f, indent=4)
            
    