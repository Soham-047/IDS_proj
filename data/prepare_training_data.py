import pandas as pd

# -----------------------------
# CONFIGURATION (MATCH LIVE)
# -----------------------------
WINDOW_SIZE_FLOWS = 20  # approx flows per 5 seconds (empirical)
DURATION_SCALE = 1_000_000  # microseconds → seconds

# -----------------------------
# LOAD DATASET
# -----------------------------
df = pd.read_csv(
    "raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
)
# Normalize column names
df.columns = df.columns.str.strip()

# Debug print (temporary)
print(df.columns.tolist())

# Convert duration to seconds
df["Flow Duration"] = df["Flow Duration"] / DURATION_SCALE

# Sort to simulate time order
df = df.reset_index(drop=True)

# -----------------------------
# WINDOW AGGREGATION
# -----------------------------
windows = []
labels = []

for start in range(0, len(df), WINDOW_SIZE_FLOWS):
    window = df.iloc[start:start + WINDOW_SIZE_FLOWS]

    if len(window) == 0:
        continue

    flow_count = len(window)
    orig_bytes_sum = window["Total Length of Fwd Packets"].sum()
    resp_bytes_sum = window["Total Length of Bwd Packets"].sum()
    avg_duration = window["Flow Duration"].mean()

    # Label logic: if ANY flow is attack → window is attack
    label = 1 if any(window["Label"] != "BENIGN") else 0

    windows.append([
        flow_count,
        orig_bytes_sum,
        resp_bytes_sum,
        avg_duration
    ])
    labels.append(label)

# -----------------------------
# FINAL TRAINING DATAFRAME
# -----------------------------
training_df = pd.DataFrame(
    windows,
    columns=[
        "flow_count",
        "orig_bytes_sum",
        "resp_bytes_sum",
        "avg_duration"
    ]
)

training_df["label"] = labels

training_df.to_csv("training_windows.csv", index=False)

print("Training dataset created")
print(training_df.head())
print("Shape:", training_df.shape)

