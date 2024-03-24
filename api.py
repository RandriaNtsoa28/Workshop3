from flask import Flask, request, jsonify
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

app = Flask(__name__)

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the KNN classifiers
knn_model1 = KNeighborsClassifier(n_neighbors=3)
knn_model1.fit(X_train, y_train)

knn_model2 = KNeighborsClassifier(n_neighbors=5)
knn_model2.fit(X_train, y_train)

# Evaluate the models
y_pred_model1 = knn_model1.predict(X_test)
accuracy_model1 = accuracy_score(y_test, y_pred_model1)
print("Model 1 Accuracy:", accuracy_model1)

y_pred_model2 = knn_model2.predict(X_test)
accuracy_model2 = accuracy_score(y_test, y_pred_model2)
print("Model 2 Accuracy:", accuracy_model2)

species_mapping = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}

# Define route for predictions from Model 1
@app.route('/predict_model1', methods=['GET'])
def predict_model1():
    # Get model arguments from the request query parameters
    sepal_length = float(request.args.get('sepal_length'))
    sepal_width = float(request.args.get('sepal_width'))
    petal_length = float(request.args.get('petal_length'))
    petal_width = float(request.args.get('petal_width'))
    
    # Make prediction using Model 1
    prediction = knn_model1.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]

    # Return prediction in a standardized format
    return jsonify({'prediction_model1': species_mapping[int(prediction)]})

# Define route for predictions from Model 2
@app.route('/predict_model2', methods=['GET'])
def predict_model2():
    # Get model arguments from the request query parameters
    sepal_length = float(request.args.get('sepal_length'))
    sepal_width = float(request.args.get('sepal_width'))
    petal_length = float(request.args.get('petal_length'))
    petal_width = float(request.args.get('petal_width'))
    
    # Make prediction using Model 2
    prediction = knn_model2.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]

    # Return prediction in a standardized format
    return jsonify({'prediction_model2': species_mapping[int(prediction)]})

if __name__ == '__main__':
    app.run(debug=True)
