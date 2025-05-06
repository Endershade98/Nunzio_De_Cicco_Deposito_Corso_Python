import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


def elimina_feature_vif_pval(X, y, soglia_vif=5.0, soglia_pval=0.05, verbose=True):
    """
    Elimina ricorsivamente le feature con alto VIF o p-value non significativo.

    Parametri:
    ----------
    X : DataFrame
        Matrice delle feature.
    y : Series
        Variabile target.
    soglia_vif : float, default=5.0
        Soglia sopra cui una variabile è considerata collineare.
    soglia_pval : float, default=0.05
        Soglia sopra cui una variabile non è statisticamente significativa.
    verbose : bool
        Se True, stampa le feature eliminate e i motivi.

    Restituisce:
    -----------
    X_ridotto : DataFrame
        Feature selezionate (senza multicollinearità né variabili non significative).
    """
    
    # Copia di X per non modificare direttamente l'input
    X_ridotto = X.copy()

    # Loop per iterare fino a che non vengono più rimosse feature
    while True:
        
        # Aggiungi una costante (intercetta) per la regressione OLS
        X_const = sm.add_constant(X_ridotto)
        
        # Adatta un modello di regressione OLS
        model = sm.OLS(y, X_const).fit()
        
        # Estrai i p-value per ogni variabile
        pvalues = model.pvalues.drop('const')  # Rimuove l'intercetta, che non ci interessa
        
        # Calcolo del VIF (Variance Inflation Factor)
        vif_data = pd.DataFrame()
        vif_data["Feature"] = X_const.columns
        vif_data["VIF"] = [variance_inflation_factor(X_const.values, i) 
                           for i in range(X_const.shape[1])]
        vif_data = vif_data.set_index("Feature").drop("const")  # Rimuove la costante

        # Verifica se ci sono feature con p-value troppo alto
        max_pval = pvalues.max()
        if max_pval > soglia_pval:
            # Trova la feature con il massimo p-value
            feature_da_rimuovere = pvalues.idxmax()
            if verbose:
                print(f"Rimuovo '{feature_da_rimuovere}' per p-value alto: {max_pval:.4f}")
            X_ridotto.drop(columns=[feature_da_rimuovere], inplace=True)
            continue  # Continua la ricerca di nuove variabili da eliminare

        # Verifica se ci sono feature con VIF troppo alto
        max_vif = vif_data["VIF"].max()
        if max_vif > soglia_vif:
            # Trova la feature con il massimo VIF
            feature_da_rimuovere = vif_data["VIF"].idxmax()
            if verbose:
                print(f"Rimuovo '{feature_da_rimuovere}' per VIF alto: {max_vif:.2f}")
            X_ridotto.drop(columns=[feature_da_rimuovere], inplace=True)
            continue  # Continua la ricerca di nuove variabili da eliminare

        # Se non ci sono più variabili da rimuovere, esci dal ciclo
        break

    return X_ridotto

# ============== VERSIONE DI MICHEAL ================

def elimina_variabili_vif_pvalue(X_train, y_train, vif_threshold=10.0, pvalue_threshold=0.05):
    """
    Rimuove variabili da X_train basandosi su VIF e p-value.
    
    - Elimina solo variabili con VIF > soglia e p-value > soglia.
    - Ricalcola VIF e p-value dopo ogni eliminazione.
    """
    
    # Copia dei dati per lavorare in sicurezza
    X_current = X_train.copy()
    
    # Aggiungi costante per statsmodels
    X_const = sm.add_constant(X_current)
    
    while True:
        # Modello OLS per calcolare p-value
        model = sm.OLS(y_train, X_const).fit()
        pvalues = model.pvalues.drop('const')  # escludi l'intercetta
        
        # Calcolo VIF
        vif = pd.DataFrame()
        vif["Feature"] = X_current.columns
        vif["VIF"] = [variance_inflation_factor(X_current.values, i) for i in range(X_current.shape[1])]
        
        # Unisco p-value e VIF
        stats = vif.copy()
        stats["p-value"] = pvalues.values
        
        # Trova candidati da eliminare: VIF alto + p-value alto
        candidates = stats[(stats["VIF"] > vif_threshold) & (stats["p-value"] > pvalue_threshold)]
        
        if candidates.empty:
            print("\nNessuna variabile da eliminare. Selezione completata.")
            break
        
        # Elimina la variabile con il VIF piÃ¹ alto tra i candidati
        worst_feature = candidates.sort_values(by="VIF", ascending=False)["Feature"].iloc[0]
        print(f"Rimuovo '{worst_feature}' con VIF = {candidates.loc[candidates['Feature'] == worst_feature, 'VIF'].values[0]:.2f} "
              f"e p-value = {candidates.loc[candidates['Feature'] == worst_feature, 'p-value'].values[0]:.4f}")
        
        # Aggiorna i dati
        X_current = X_current.drop(columns=[worst_feature])
        X_const = sm.add_constant(X_current)
    
    print("\nFeature finali selezionate:")
    print(X_current.columns.tolist())
    
    return X_current