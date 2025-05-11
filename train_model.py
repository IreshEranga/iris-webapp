import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pickle

iris = load_iris()
X, y = iris.data, iris.target

model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open('model/iris_model.pkl', 'wb') as f:
    pickle.dump(model, f)
