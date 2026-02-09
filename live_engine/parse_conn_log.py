import pandas as pd

LOG_FILE = "/Users/bomboclat/Desktop/IDS Project/flowguard/flowguard_live/conn.log"

columns = [
    "ts","uid","src_ip","src_port",
    "dst_ip","dst_port","proto",
    "service","duration","orig_bytes","resp_bytes"
]

# Read Zeek conn.log
df = pd.read_csv(
    LOG_FILE,
    sep="\t",
    comment="#",
    names=columns,
    usecols=range(len(columns))
)
df = df.dropna()
df["duration"] = pd.to_numeric(df["duration"], errors="coerce")
df["orig_bytes"] = pd.to_numeric(df["orig_bytes"], errors="coerce")
df["resp_bytes"] = pd.to_numeric(df["resp_bytes"], errors="coerce")

df = df.dropna()
print(df[["src_ip","dst_ip","proto","duration","orig_bytes","resp_bytes"]].head())
print("Total Flows:", len(df))
print(df.dtypes)

