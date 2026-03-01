import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

MODEL_PATH = "backend/model.joblib"

def train_model():
    np.random.seed(42)

    # Fake vibration data
    X = np.random.rand(500, 3)
    y = 0.5 * X[:, 0] + 0.3 * X[:, 1] + 0.2 * X[:, 2]

    model = LinearRegression()
    model.fit(X, y)

    joblib.dump(model, MODEL_PATH)

def predict(vib_x, vib_y, vib_z):
    model = joblib.load(MODEL_PATH)
    X = np.array([[vib_x, vib_y, vib_z]])
    return float(model.predict(X)[0])
