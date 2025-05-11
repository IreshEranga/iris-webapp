from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.datasets import load_iris
iris_data = load_iris()

app = Flask(__name__)
model = pickle.load(open('model/iris_model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    prediction = model.predict([features])[0]
    species = iris_data.target_names[prediction]
    return render_template('index.html', prediction_text=f'Predicted species: {species.capitalize()}')

if __name__ == '__main__':
    app.run(debug=True)
