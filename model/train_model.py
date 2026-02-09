import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
import joblib

# --------------------------------
# PATH SETUP
# --------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "training_windows.csv")
MODEL_PATH = os.path.join(BASE_DIR, "model", "model.pkl")

# --------------------------------
# LOAD DATA
# --------------------------------
df = pd.read_csv(DATA_PATH)

X = df[[
    "flow_count",
    "orig_bytes_sum",
    "resp_bytes_sum",
    "avg_duration"
]]

y = df["label"]

# --------------------------------
# TRAIN / TEST SPLIT
# --------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# --------------------------------
# MODEL TRAINING
# --------------------------------
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# --------------------------------
# EVALUATION
# --------------------------------
y_pred = model.predict(X_test)

print("\n=== Classification Report ===")
print(classification_report(y_test, y_pred))

print("\n=== Confusion Matrix ===")
print(confusion_matrix(y_test, y_pred))

# --------------------------------
# SAVE MODEL
# --------------------------------
joblib.dump(model, MODEL_PATH)
print("\n✅ Model saved to:", MODEL_PATH)

