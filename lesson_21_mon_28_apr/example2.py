# Importare le librerie necessarie
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Caricare il dataset Iris
iris = load_iris()
X = iris.data # Caratteristiche (lunghezza e larghezza di sepali e petali)
y = iris.target # Etichette (specie di Iris)

# Suddividere il dataset in set di training e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Definire il modello: K-Nearest Neighbors Classifier
model = KNeighborsClassifier(n_neighbors=3)

# Addestrare il modello sui dati di training
model.fit(X_train, y_train)

# Fare predizioni sui dati di test
y_pred = model.predict(X_test)

# Valutare le prestazioni del modello
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza del modello: {accuracy:.2f}")


random_states = [42, 100, 1000]
n_neighbor_list = [1, 3, 11]

for state in random_states:
    # Suddividere il dataset in set di training e test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=state)
    for n in n_neighbor_list:
    # Definire il modello: K-Nearest Neighbors Classifier
        model = KNeighborsClassifier(n_neighbors=3)

    # Addestrare il modello sui dati di training
        model.fit(X_train, y_train)

    # Fare predizioni sui dati di test
        y_pred = model.predict(X_test)

    # Valutare le prestazioni del modello
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuratezza del modello: {accuracy:.2f}")


def modelling(state = 42, n_neighbor = 3):
    # Suddividere il dataset in set di training e test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=state)
    # Definire il modello: K-Nearest Neighbors Classifier
    model = KNeighborsClassifier(n_neighbors=n_neighbor)

    # Addestrare il modello sui dati di training
    model.fit(X_train, y_train)

    # Fare predizioni sui dati di test
    y_pred = model.predict(X_test)

    # Valutare le prestazioni del modello
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuratezza del modello: {accuracy:.2f}")


for x in random_states:
    modelling(x)