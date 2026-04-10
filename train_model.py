"""
Train a Random Forest classifier on sample flood data.
Run this once before starting the Flask app:
    python train_model.py
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

# Extended training data
data = {
    "rainfall":    [10,  30,  50,  80,  100, 120, 150, 180, 200, 220, 250, 280, 300, 15,  60,  90,  130, 170, 210, 260],
    "water_level": [0.5, 1.5, 3,   4,   5,   6,   7.5, 9,   10,  11,  12,  14,  15,  0.8, 3.2, 4.5, 6.5, 8.5, 10.5, 13],
    "humidity":    [55,  60,  70,  75,  78,  80,  84,  87,  90,  91,  93,  94,  95,  58,  72,  76,  82,  86,  91,  94],
    "flood":       [0,   0,   0,   0,   0,   0,   1,   1,   1,   1,   1,   1,   1,   0,   0,   0,   1,   1,   1,   1],
}

df = pd.DataFrame(data)
X = df[["rainfall", "water_level", "humidity"]]
y = df["flood"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

print("=== Model Evaluation ===")
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred, target_names=["Safe", "Flood"]))

pickle.dump(model, open("flood_model.pkl", "wb"))
print("✓ Model saved to flood_model.pkl")
