import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import classification_report, confusion_matrix

# === 1. Caricamento e preparazione del dataset ===
iris = load_iris()
X = iris.data
y = iris.target

# Standardizzazione
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

# === 2. Grid Search per KNN ===
knn = KNeighborsClassifier()
param_grid_knn = {
    'n_neighbors': [1, 3, 5, 7, 9],
    'weights': ['uniform', 'distance'],
    'metric': ['euclidean', 'manhattan']
}

grid_knn = GridSearchCV(knn, param_grid_knn, cv=5, scoring='accuracy')
grid_knn.fit(X_train, y_train)

best_knn = grid_knn.best_estimator_
y_pred_knn = best_knn.predict(X_test)

print("\n=== Migliori parametri KNN ===")
print(grid_knn.best_params_)
print("\n=== Classification Report - KNN ===")
print(classification_report(y_test, y_pred_knn, target_names=iris.target_names))

# Confusion matrix - KNN
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred_knn), annot=True, fmt='d',
            cmap='YlGnBu', xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.title("Confusion Matrix - KNN")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

# === 3. Grid Search per Decision Tree ===
tree = DecisionTreeClassifier(random_state=42)
param_grid_tree = {
    'criterion': ['gini', 'entropy'],
    'max_depth': [2, 3, 4, 5, None],
    'min_samples_split': [2, 3, 4],
    'min_samples_leaf': [1, 2, 3]
}

grid_tree = GridSearchCV(tree, param_grid_tree, cv=5, scoring='accuracy')
grid_tree.fit(X_train, y_train)

best_tree = grid_tree.best_estimator_
y_pred_tree = best_tree.predict(X_test)

print("\n=== Migliori parametri Decision Tree ===")
print(grid_tree.best_params_)
print("\n=== Classification Report - Decision Tree ===")
print(classification_report(y_test, y_pred_tree, target_names=iris.target_names))

# Confusion matrix - Decision Tree
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_test, y_pred_tree), annot=True, fmt='d',
            cmap='Oranges', xticklabels=iris.target_names,
            yticklabels=iris.target_names)
plt.title("Confusion Matrix - Decision Tree")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

# === 4. Visualizzazione dell’albero decisionale migliore ===
plt.figure(figsize=(12, 6))
plot_tree(best_tree, feature_names=iris.feature_names,
          class_names=iris.target_names, filled=True)
plt.title("Best Decision Tree")
plt.tight_layout()
plt.show()
