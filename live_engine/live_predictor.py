import os
import time
import joblib
import pandas as pd

from window_aggregator import add_flow, aggregate_features

# --------------------------------
# PATH SETUP
# --------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_FILE = os.path.join(
    BASE_DIR,
    "flowguard_live",
    "conn.log"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "model",
    "model.pkl"
)

# --------------------------------
# LOAD MODEL
# --------------------------------
model = joblib.load(MODEL_PATH)
print("✅ ML model loaded")

# --------------------------------
# STREAM ZEEK LOG (TAIL)
# --------------------------------
def stream_zeek_logs(file_path):
    with open(file_path, "r") as f:
        f.seek(0, os.SEEK_END)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            if line.startswith("#"):
                continue
            yield line


# --------------------------------
# LIVE PREDICTION LOOP
# --------------------------------
print("🚀 Starting LIVE intrusion detection...\n")
print("⏳ Waiting for flows to accumulate...\n")

for line in stream_zeek_logs(LOG_FILE):
    parts = line.strip().split("\t")

    try:
        duration = parts[8]
        orig_bytes = parts[9]
        resp_bytes = parts[10]

        # Skip invalid flows
        if duration == "-" or orig_bytes == "-" or resp_bytes == "-":
            continue

        flow = {
            "duration": float(duration),
            "orig_bytes": float(orig_bytes),
            "resp_bytes": float(resp_bytes)
        }

    except (IndexError, ValueError):
        continue

    add_flow(flow)

    features = aggregate_features()

    if features:
        prediction = model.predict([features])[0]

        if prediction == 1:
            print("🚨 ALERT: Malicious behavior detected")
        else:
            print("✅ Traffic normal")

