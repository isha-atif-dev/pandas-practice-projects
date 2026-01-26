import pandas as pd

# --------------------------------------------------
# 1. Load dataset
# --------------------------------------------------
# Reading the real-world DDoS network traffic dataset.
# This dataset contains flow-level features for benign and attack traffic.

df = pd.read_csv("03_real_world_analysis/dataset/ddos.csv")


# --------------------------------------------------
# 2. Basic inspection (structure understanding)
# --------------------------------------------------
# These checks help understand the size, columns, and data types.
# Uncomment when needed during exploration.

# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.head())


# --------------------------------------------------
# 3. Data quality checks
# --------------------------------------------------

# --- Duplicate rows ---
# Network traffic datasets often contain duplicate flows due to
# repeated logging or aggregation at capture time.

duplicated_count = df.duplicated().sum()
print("Duplicated rows:", duplicated_count)

print("Rows before removing duplicates:", df.shape[0])

# Remove exact duplicate rows to improve data quality
df = df.drop_duplicates()

print("Rows after removing duplicates:", df.shape[0])


# --------------------------------------------------
# 4. Check for weird / invalid values
# --------------------------------------------------
# Weird values are values that do not make sense in real-world networking,
# such as:
# - Negative flow duration
# - Negative packet or byte counts
# - Impossible timing values

# Example: check if Flow Duration contains negative values
print((df[" Flow Duration"] < 0).sum())


# --------------------------------------------------
# 5. Handle negative values across numeric features
# --------------------------------------------------
# Select only numeric columns to avoid touching categorical data (e.g., labels)

numeric_cols = df.select_dtypes(include="number")

# Count how many negative values exist per numeric column
# negative_counts = (numeric_cols < 0).sum()
# print(negative_counts[negative_counts > 0])

# Replace all negative numeric values with 0
# This ensures no invalid negative metrics remain in the dataset
df[numeric_cols.columns] = df[numeric_cols.columns].clip(lower=0)

# Re-check summary statistics after cleaning
print(df.describe())


# --------------------------------------------------
# 6. Attack vs Benign traffic analysis (CORE SECTION)
# --------------------------------------------------

# Check how many samples exist per traffic class
print(df[" Label"].value_counts())

# Compare average behaviour of network metrics
# across benign and different attack types
grouped_stats = df.groupby(" Label").mean()
print(grouped_stats)


# --------------------------------------------------
# 7. Save outputs (data pipeline step)
# --------------------------------------------------
# Save attack vs benign summary statistics
grouped_stats.to_csv(
    "03_real_world_analysis/outputs/attack_vs_benign_means.csv"
)

# Save the cleaned dataset for downstream analysis or modeling
df.to_csv(
    "03_real_world_analysis/outputs/cleaned_ddos.csv",
    index=False
)
