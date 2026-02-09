import time
import pandas as pd
from window_aggregator import add_flow, aggregate_features

LOG_FILE = "/Users/bomboclat/Desktop/IDS Project/flowguard/flowguard_live/conn.log"

columns = [
    "ts","uid","src_ip","src_port",
    "dst_ip","dst_port","proto",
    "service","duration","orig_bytes","resp_bytes"
]

df = pd.read_csv(
    LOG_FILE,
    sep="\t",
    comment="#",
    names=columns,
    usecols=range(len(columns))
)

df = df.dropna()

for _, row in df.iterrows():

    # Skip invalid Zeek values
    if row["duration"] == "-" or row["orig_bytes"] == "-" or row["resp_bytes"] == "-":
        continue

    try:
        flow = {
            "duration": float(row["duration"]),
            "orig_bytes": float(row["orig_bytes"]),
            "resp_bytes": float(row["resp_bytes"])
        }
    except ValueError:
        continue

    add_flow(flow)
    features = aggregate_features()

    if features:
        print(features)

    time.sleep(0.5)

