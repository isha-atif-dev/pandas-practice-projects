## Real-World DDoS Analysis

This project demonstrates a real-world data analysis workflow using **Pandas** on a DDoS network traffic dataset.  
The focus is on understanding raw network flow data, improving data quality, and comparing behavioural patterns between **benign** and **attack** traffic.

---

## Dataset Notice

The dataset used in this analysis exceeds GitHub’s file size limit and is therefore **not included** in this repository.

You can download a similar publicly available dataset from:
- https://www.unb.ca/cic/datasets/

After downloading, place the CSV file in the following directory before running the analysis:



---

## What This Analysis Covers

This project reflects **real-world security data challenges**

### 1. Data Loading
- Loads flow-level DDoS traffic data using Pandas
- Handles large CSV files commonly seen in cybersecurity datasets

### 2. Data Inspection
- Examines dataset structure, columns, and data types
- Helps understand traffic features before any modelling

### 3. Data Quality Checks
- Identifies duplicate network flows
- Removes exact duplicates caused by repeated logging or aggregation

### 4. Invalid / Weird Value Detection
Checks for values that do not make sense in real networking scenarios, such as:
- Negative flow duration
- Negative packet or byte counts

### 5. Data Cleaning
- Selects numeric features only
- Replaces invalid negative values with zero
- Ensures realistic and ML-safe data

### 6. Attack vs Benign Traffic Analysis
- Groups traffic by label
- Computes mean statistics for each traffic class
- Highlights behavioural differences between benign traffic and DDoS attacks

This section represents the **core analytical insight** of the project.

### 7. Output Generation
The analysis produces reusable outputs:
- A cleaned dataset for downstream processing
- A CSV file containing mean statistics per traffic class

These outputs can be directly used for:
- Machine learning pipelines  
- Feature engineering  
- Visualisation  
- Explainable AI experiments (e.g. SHAP)

---

## Project Structure

03_real_world_analysis/
│
├── dataset/
│ └── ddos.csv
│
├── outputs/
│ ├── cleaned_ddos.csv
│ └── attack_vs_benign_means.csv
│
├── analysis.py
└── README.md

## Why This Project Matters

- Network traffic data is often noisy, duplicated, and contains invalid values
- Real-world cybersecurity datasets must be cleaned and validated before they can be trusted for analysis or machine learning
- Demonstrates practical data preparation steps required before modelling or deployment

- Mirrors early stages of:
  - Intrusion detection research
  - Security analytics
  - Machine learning feature engineering
  - Explainable AI pipelines

## Skills Demonstrated

- Pandas data manipulation
- Real-world data cleaning and validation
- Handling duplicate records and invalid values
- Group-based statistical analysis
- Reproducible data pipelines
- Cybersecurity-focused data reasoning
