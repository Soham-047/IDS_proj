# 🛡️ FlowGuard  
## Real-Time Machine Learning–Based Network Intrusion Detection System

---

## 📌 Overview

**FlowGuard** is a **truly live Network Intrusion Detection System (IDS)** that performs **continuous machine learning inference** on **real-time network traffic**.

Unlike traditional IDS implementations that rely on offline datasets or traffic replay, FlowGuard operates on **live network flows**, making real-time security decisions using a trained ML model.

---

## 🧠 System Architecture

Live Network Traffic
↓
Zeek
↓
Flow Logs (conn.log)
↓
Sliding Window Aggregation
↓
Feature Vector
↓
ML Model
↓
ALERT / NORMAL

yaml
Copy code

---

## 📂 Project Structure

flowguard/
├── data/
│ ├── raw/
│ │ └── Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv
│ └── training_windows.csv
│
├── flowguard_live/
│ └── conn.log
│
├── live_engine/
│ ├── parse_conn_log.py
│ ├── window_aggregator.py
│ ├── live_predictor.py
│ └── fake_attack.py
│
├── model/
│ ├── train_model.py
│ └── model.pkl
│
├── venv/
└── README.md

yaml
Copy code

---

## ⚙️ Setup

### 1️⃣ Create Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
2️⃣ Install Dependencies
```bash

pip install pandas numpy scikit-learn joblib