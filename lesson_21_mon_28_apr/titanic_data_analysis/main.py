import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import r2_score

from titanic import (
    load_and_clean_data, plot_correlation_heatmap, plot_feature_importance,
    evaluate_model, plot_boxplots, remove_outliers_iqr
)

# Percorso al dataset
DATA_PATH = '/home/endershade/Desktop/Python_Course_Repo/lesson_21_mon_28_apr/titanic_data_analysis/titanic_train_data.csv'

# Caricamento iniziale dei dati
df = None
X_train, X_test, y_train, y_test = None, None, None, None


def menu():
    print("\n--- MENU ANALISI TITANIC ---")
    print("1. Carica e pulisci il dataset")
    print("2. Visualizza heatmap di correlazione")
    print("3. Allenamento Random Forest e importanza feature")
    print("4. Allenamento Decision Tree e valutazione")
    print("5. Ottimizzazione Decision Tree (GridSearch)")
    print("6. Logistic Regression")
    print("7. Linear Regression (R²)")
    print("8. Visualizza boxplot delle feature")
    print("9. Rimuovi outlier (IQR)")
    print("0. Esci")


def main():
    global df, X_train, X_test, y_train, y_test
    tree_model = None

    while True:
        menu()
        choice = input("Seleziona un'opzione: ")

        if choice == '1':
            df = load_and_clean_data(DATA_PATH)
            X = df.drop('Survived', axis=1)
            y = df['Survived']
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            print("Dataset caricato e pulito.")

        elif choice == '2':
            if df is not None:
                plot_correlation_heatmap(df)
            else:
                print("Carica prima il dataset.")

        elif choice == '3':
            if X_train is not None:
                model = RandomForestClassifier(n_estimators=100, random_state=42)
                model.fit(X_train, y_train)
                plot_feature_importance(model, X_train.columns)
            else:
                print("Carica prima il dataset.")

        elif choice == '4':
            if X_train is not None:
                tree_model = DecisionTreeClassifier(max_depth=4, random_state=42)
                tree_model.fit(X_train, y_train)
                y_pred = tree_model.predict(X_test)
                evaluate_model(y_test, y_pred, ['Not Survived', 'Survived'], 'Decision Tree')
            else:
                print("Carica prima il dataset.")

        elif choice == '5':
            if X_train is not None:
                from sklearn.model_selection import GridSearchCV
                param_grid = {
                    'max_depth': [3, 4, 5],
                    'min_samples_split': [2, 5],
                    'min_samples_leaf': [1, 2],
                    'criterion': ['gini', 'entropy']
                }
                grid = GridSearchCV(DecisionTreeClassifier(random_state=42), param_grid, cv=3)
                grid.fit(X_train, y_train)
                print("Best params:", grid.best_params_)
                y_pred = grid.best_estimator_.predict(X_test)
                evaluate_model(y_test, y_pred, ['Not Survived', 'Survived'], 'Decision Tree Ottimizzato')
            else:
                print("Carica prima il dataset.")

        elif choice == '6':
            if X_train is not None:
                logreg = LogisticRegression(max_iter=1000)
                logreg.fit(X_train, y_train)
                y_pred = logreg.predict(X_test)
                evaluate_model(y_test, y_pred, ['Not Survived', 'Survived'], 'Logistic Regression')
            else:
                print("Carica prima il dataset.")

        elif choice == '7':
            if X_train is not None:
                linreg = LinearRegression()
                linreg.fit(X_train, y_train)
                y_pred = linreg.predict(X_test)
                r2 = r2_score(y_test, y_pred)
                print(f"R² Linear Regression: {r2:.4f}")
            else:
                print("Carica prima il dataset.")

        elif choice == '8':
            if df is not None:
                plot_boxplots(df)
            else:
                print("Carica prima il dataset.")

        elif choice == '9':
            if df is not None:
                df = remove_outliers_iqr(df)
                print("Outlier rimossi.")
            else:
                print("Carica prima il dataset.")

        elif choice == '0':
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida. Riprovare.")


if __name__ == "__main__":
    main()
