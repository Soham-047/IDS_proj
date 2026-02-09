import pandas as pd

df = pd.read_csv(
    "raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
)

print("Total rows:", len(df))
print("\n=== COLUMN NAMES (exact) ===")
for col in df.columns:
    print(repr(col))

