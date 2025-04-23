import numpy as np



def prepara_dati_per_modello(df):
    # Converte la colonna 'Churn': "No" → 0, "Sì" → 1
    df['Churn'] = df['Churn'].map({'No': 0, 'Sì': 1})
    
    # Crea la colonna 'Costo_per_GB' evitando divisione per 0
    if 'Costo_per_GB' not in df.columns:
        df['Costo_per_GB'] = df.apply(
            lambda row: row['Tariffa_Mensile'] / row['Dati_Consumati'] if row['Dati_Consumati'] > 0 else 0,
            axis=1
        )
    
    # Colonne da normalizzare
    colonne_numeriche = [
        'Età', 'Durata_Abbonamento', 'Tariffa_Mensile',
        'Dati_Consumati', 'Servizio_Clienti_Contatti', 'Costo_per_GB'
    ]
    
    for col in colonne_numeriche:
        minimo = df[col].min()
        massimo = df[col].max()
        df[col + '_norm'] = (df[col] - minimo) / (massimo - minimo)
    
    return df

