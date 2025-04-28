from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler # import per la standardizzazione dei dati
from sklearn.tree import DecisionTreeClassifier  # import del DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix # import di classification report e confusion matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Carichiamo il dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Standardizziamo le caratteristiche
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Suddividiamo in training e test set (70% training, 30% test)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Creiamo e alleniamo il modello Decision Tree
dtc = DecisionTreeClassifier(random_state=42)
dtc.fit(X_train, y_train)

# Facciamo le predizioni sul test set
y_pred = dtc.predict(X_test)

# Valutiamo la performance con classification report
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))

# Visualizziamo la matrice di confusione
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(8,6))
sns.heatmap(cm, annot=True, cmap="Blues", fmt='d', 
            xticklabels=iris.target_names, 
            yticklabels=iris.target_names)
plt.title('Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.show()


class ConfusionAnalyser:
    
    def __init__(self, dataset, random_state, test_size):
        self.dataset = dataset = load_iris()
        self.X = self.dataset.data
        self.y = self.dataset.target
        self.state = random_state
        self.test_size = test_size
        
    def standardize(self):
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(self.X)
        return X_scaled
        
    def divide_train_test(self, X_scaled):
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)
        return X_train, X_test, y_train, y_test 
    
    
    
    