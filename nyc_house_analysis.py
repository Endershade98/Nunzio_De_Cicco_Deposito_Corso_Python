# =====================================
# 1. Import delle librerie
# =====================================
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

# =====================================
# 2. Funzioni modulari
# =====================================

def compute_vif(X: pd.DataFrame) -> pd.DataFrame:
    """
    Calcola il VIF per ciascuna colonna di X.

    Parametri:
        X: DataFrame di feature (senza costante)
    Restituisce:
        DataFrame con colonne ['feature','VIF']
    """
    X_const = sm.add_constant(X)
    vif_data = []
    for i, col in enumerate(X_const.columns):
        if col == 'const':
            continue
        vif = variance_inflation_factor(X_const.values, i)
        vif_data.append({'feature': col, 'VIF': vif})
    return pd.DataFrame(vif_data)


def compute_pvalues(X: pd.DataFrame, y: pd.Series) -> pd.Series:
    """
    Calcola i p-value di ciascuna feature tramite OLS.

    Parametri:
        X: DataFrame di feature (senza costante)
        y: Series target
    Restituisce:
        Series di p-value indicizzati per feature
    """
    X_const = sm.add_constant(X)
    model = sm.OLS(y, X_const).fit()
    # drop p-value dell'intercetta
    return model.pvalues.drop('const')


def eliminate_features_vif_pvalue(
    X: pd.DataFrame,
    y: pd.Series,
    vif_threshold: float = 5.0,
    pvalue_threshold: float = 0.05
) -> pd.DataFrame:
    """
    Itera rimuovendo le feature con VIF > vif_threshold
    e p-value > pvalue_threshold fino a cessare rimozioni.

    Parametri:
        X: DataFrame di feature
        y: Series target
        vif_threshold: soglia VIF
        pvalue_threshold: soglia p-value

    Restituisce:
        DataFrame con le feature selezionate
    """
    X_sel = X.copy()
    while True:
        vif_df = compute_vif(X_sel)
        pvals = compute_pvalues(X_sel, y)

        # unisci VIF e p-value
        stats = vif_df.set_index('feature')
        stats['pvalue'] = pvals

        # individua feature da rimuovere
        to_remove = stats[
            (stats['VIF'] > vif_threshold) &
            (stats['pvalue'] > pvalue_threshold)
        ]
        if to_remove.empty:
            break

        # rimuovi la feature con VIF più alto
        worst = to_remove.sort_values('VIF', ascending=False).index[0]
        print(f"Rimuovo '{worst}': VIF={stats.loc[worst,'VIF']:.2f}, "
              f"p-value={stats.loc[worst,'pvalue']:.4f}")
        X_sel = X_sel.drop(columns=[worst])

    return X_sel

# =====================================
# 3. Use-case: pulizia Airbnb + selezione feature
# =====================================
if __name__ == "__main__":
    # Carica il CSV pulito (es. listings_cleaned.csv)
    df = pd.read_csv('listings_cleaned.csv')

    # Definisci target e feature
    y = df['price']
    X = df.drop(columns=['price'])

    # Seleziona feature con VIF e p-value
    X_selected = eliminate_features_vif_pvalue(
        X, y,
        vif_threshold=5.0,
        pvalue_threshold=0.05
    )

    print("\nFeature finali selezionate:")
    print(X_selected.columns.tolist())
