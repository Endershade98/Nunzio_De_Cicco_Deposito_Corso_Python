import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import r2_score

# ----------------------------- FUNZIONI UTILI -----------------------------

def load_and_clean_data(path):
    """
    Carica un dataset da file CSV e applica operazioni di pulizia di base.
    
    Parametri:
    - path (str): percorso del file CSV
    
    Restituisce:
    - pd.DataFrame: dataframe pulito e codificato
    """
    df = pd.read_csv(path)

    # Rimozione colonne inutili per la modellazione
    df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True)

    # Imputazione dei valori mancanti
    df['Age'].fillna(df['Age'].mean(), inplace=True)
    df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

    # Codifica delle variabili categoriche
    df = pd.get_dummies(df, columns=['Sex', 'Embarked'], drop_first=True)

    return df

def plot_correlation_heatmap(df, title="Matrice di Correlazione"):
    """
    Visualizza una heatmap della matrice di correlazione per le colonne numeriche.

    Parametri:
    - df (pd.DataFrame): dataframe contenente solo colonne numeriche
    - title (str): titolo del grafico
    """
    corr = df.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
    plt.title(title)
    plt.tight_layout()
    plt.show()

def plot_feature_importance(model, feature_names):
    """
    Visualizza un grafico orizzontale dell'importanza delle feature per un modello addestrato.

    Parametri:
    - model: modello di classificazione con attributo feature_importances_
    - feature_names (list): nomi delle feature
    """
    importances = model.feature_importances_
    plt.figure(figsize=(10, 6))
    plt.barh(feature_names, importances, color='seagreen')
    plt.xlabel("Importanza")
    plt.title("Importanza delle variabili (Random Forest)")
    plt.tight_layout()
    plt.show()

def evaluate_model(y_true, y_pred, labels, title):
    """
    Stampa un classification report e visualizza la confusion matrix in formato heatmap.

    Parametri:
    - y_true (array-like): valori reali
    - y_pred (array-like): predizioni del modello
    - labels (list): etichette delle classi
    - title (str): titolo del grafico
    """
    print("Classification Report:\n", classification_report(y_true, y_pred))
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=labels, yticklabels=labels)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(title)
    plt.tight_layout()
    plt.show()

def plot_boxplots(df, target='Survived'):
    """
    Visualizza boxplot per ogni feature numerica rispetto alla variabile target.

    Parametri:
    - df (pd.DataFrame): dataframe completo
    - target (str): nome della variabile target
    """
    numeric_cols = df.select_dtypes(include='number').columns.drop(target)
    plt.figure(figsize=(14, 12))
    for i, col in enumerate(numeric_cols, 1):
        plt.subplot(3, 3, i)
        sns.boxplot(x=target, y=col, data=df)
        plt.title(f'{col} vs {target}')
    plt.tight_layout()
    plt.show()

def remove_outliers_iqr(df, exclude=['Survived']):
    """
    Rimuove outlier dalle colonne numeriche usando il metodo IQR.

    Parametri:
    - df (pd.DataFrame): dataframe completo
    - exclude (list): colonne da escludere dal controllo outlier

    Restituisce:
    - pd.DataFrame: dataframe senza outlier
    """
    numeric_cols = df.select_dtypes(include='number').drop(columns=exclude).columns
    for col in numeric_cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    return df


# ----------------------------- WORKFLOW PRINCIPALE -----------------------------

# 1. Caricamento e pulizia dati
df = load_and_clean_data('/home/endershade/Desktop/Python_Course_Repo/lesson_21_mon_28_apr/titanic_data_analysis/titanic_train_data.csv')
print(df.info())

# 2. Analisi esplorativa
plot_correlation_heatmap(df.select_dtypes(include='number'), title="Correlazione con 'Survived'")
print(df.select_dtypes(include='number').corr()['Survived'].sort_values(ascending=False))

# 3. Preparazione dati
X = df.drop('Survived', axis=1)
y = df['Survived']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Random Forest: Feature importance
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
plot_feature_importance(rf, X.columns)

# 5. Decision Tree
tree = DecisionTreeClassifier(max_depth=4, random_state=42)
tree.fit(X_train, y_train)
y_pred = tree.predict(X_test)
evaluate_model(y_test, y_pred, ['Not Survived', 'Survived'], "Confusion Matrix - Decision Tree")

# Visualizzazione albero
plt.figure(figsize=(20, 10))
plot_tree(tree, feature_names=X.columns, class_names=["Not Survived", "Survived"],
          filled=True, rounded=True)
plt.title("Decision Tree")
plt.show()

# 6. Grid Search
param_grid = {
    'max_depth': [3, 4, 5, 6, 7, 8],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'criterion': ['gini', 'entropy']
}
grid_search = GridSearchCV(tree, param_grid, cv=5, scoring='accuracy', n_jobs=-1, verbose=1)
grid_search.fit(X_train, y_train)
print("Migliori parametri:", grid_search.best_params_)
print("Miglior punteggio:", grid_search.best_score_)

# 7. Valutazione miglior modello
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
evaluate_model(y_test, y_pred, ['Not Survived', 'Survived'], "Confusion Matrix - Best Tree")

# 8. Logistic Regression
logreg = LogisticRegression(max_iter=1000, random_state=42)
logreg.fit(X_train, y_train)
y_pred = logreg.predict(X_test)
evaluate_model(y_test, y_pred, ['Not Survived', 'Survived'], "Confusion Matrix - Logistic Regression")

# 9. Linear Regression: R²
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
y_pred = lin_reg.predict(X_test)
print(f"R² (Linear Regression): {r2_score(y_test, y_pred):.4f}")

# 10. Boxplot e heatmap delle feature
plot_boxplots(df)
plot_correlation_heatmap(df.drop('Survived', axis=1), title="Correlazione tra le Feature")

# 11. Outlier removal
df_clean = remove_outliers_iqr(df)
