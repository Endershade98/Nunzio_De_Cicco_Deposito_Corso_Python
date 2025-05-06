from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error


def load_data():
    """Load the California housing dataset.
    """
    housing = fetch_california_housing()
    return housing.data, housing.target

def split_data(X, y):
    X_train_full, X_test, y_train_full, y_test = train_test_split(X, y, random_state=42)
    X_train, X_valid, y_train, y_valid = train_test_split(X_train_full, y_train_full, random_state=42)
    return X_train, X_valid, X_test, y_train, y_valid, y_test

def build_pipeline():
    mlp_reg = MLPRegressor(hidden_layer_sizes=[50, 50, 50],
                           activation='relu',
                           solver='adam',
                           alpha=0.0001,
                           max_iter=500,
                           random_state=42)
    return make_pipeline(StandardScaler(), mlp_reg)

def evaluate_model(pipeline, X_valid, y_valid):
    y_pred = pipeline.predict(X_valid)
    mse = mean_squared_error(y_valid, y_pred)
    rmse = mse ** 0.5
    print(f"Root Mean Squared Error (Validation): {rmse:.3f}")

def main():
    X, y = load_data()
    X_train, X_valid, X_test, y_train, y_valid, y_test = split_data(X, y)
    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)
    evaluate_model(pipeline, X_valid, y_valid)

if __name__ == '__main__':
    main()