## FlowGuard – Real-Time Machine Learning–Based Network Intrusion Detection System

# OVERVIEW
FlowGuard is a truly live network intrusion detection system (IDS) that performs continuous machine learning inference on real-time network traffic.

# SYSTEM ARCHITECTURE
Live Network Traffic → Zeek → Flow Logs → Sliding Window → ML Model → Alert/Normal

# PROJECT STRUCTURE
flowguard/
├── data/
│   ├── raw/
│   │   └── Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
│   └── training_windows.csv
├── flowguard_live/
│   └── conn.log
├── live_engine/
│   ├── parse_conn_log.py
│   ├── window_aggregator.py
│   ├── live_predictor.py
│   └── fake_attack.py
├── model/
│   ├── train_model.py
│   └── model.pkl
├── venv/
└── README.md

# SETUP
python3 -m venv venv
source venv/bin/activate
pip install pandas numpy scikit-learn joblib

# DATASET
Download CIC-IDS2017 from:
https://www.kaggle.com/datasets/chethuhn/network-intrusion-dataset

# USAGE
python data/prepare_training_data.py
python model/train_model.py
sudo zeek -i en0
python live_engine/live_predictor.py

# FEATURE SCHEMA
[flow_count, orig_bytes_sum, resp_bytes_sum, avg_duration]


