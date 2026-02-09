# 🛡️ FlowGuard  
### Real-Time Machine Learning–Based Network Intrusion Detection System

FlowGuard is a high-performance, live Network Intrusion Detection System (NIDS). Unlike traditional systems that analyze static PCAP files, FlowGuard performs **continuous ML inference** on active network streams, allowing for immediate identification and mitigation of threats as they happen.

---

## 📌 Overview

FlowGuard bridges the gap between deep packet inspection and predictive analytics. By leveraging **Zeek** for metadata extraction and a **Sliding Window Aggregator**, it transforms raw network packets into actionable feature vectors for real-time security decision-making.

### Key Features
* **Live Traffic Analysis:** No more offline replay; analyze packets as they hit the interface.
* **Behavioral Detection:** Uses ML to find patterns, not just static signatures.
* **Automated Feature Engineering:** Real-time sliding window aggregation of `conn.log` data.

---

## 🧠 System Architecture

FlowGuard follows a linear pipeline from wire to decision:



1.  **Ingestion:** Zeek monitors the network interface and generates `conn.log`.
2.  **Processing:** `parse_conn_log.py` extracts raw flow data.
3.  **Transformation:** `window_aggregator.py` groups logs into time-based windows.
4.  **Inference:** `live_predictor.py` feeds the feature vector into the trained ML model.
5.  **Output:** Immediate `ALERT` or `NORMAL` classification.

---

## 📂 Project Structure

```text
flowguard/
├── data/
│   ├── raw/                 # Original datasets (e.g., CIC-IDS2017)
│   └── training_windows.csv # Processed data for model training
├── flowguard_live/
│   └── conn.log             # Active log file being watched by the engine
├── live_engine/
│   ├── parse_conn_log.py    # Log parser
│   ├── window_aggregator.py # Sliding window logic
│   ├── live_predictor.py    # Real-time inference script
│   └── fake_attack.py       # Script to simulate traffic for testing
├── model/
│   ├── train_model.py       # ML Training pipeline
│   └── model.pkl            # Serialized trained model
└── README.md
```
# ⚙️ Setup & Installation
## Create Virtual Environment
```
python3 -m venv venv
```
## Activate Environment
## On macOS/Linux:
```
source venv/bin/activate
```
## On Windows:
```
.\venv\Scripts\activate
```
## Install Dependencies
```
pip install pandas numpy scikit-learn joblib
```
## Launch Predictor(After training model train_model.py)
```bash
cd flowguard/flowguard_live
sudo zeek -i en0
cd flowguard
python live_engine/live_predictor.py
```
