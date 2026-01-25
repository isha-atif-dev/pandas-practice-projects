# ------------------------------------------------------------
# missing_data.py
# This script focuses on detecting and handling missing values
# in a dataset using pandas.
# ------------------------------------------------------------

import pandas as pd

# ------------------------------------------------------------
# Load the raw dataset
# This dataset contains missing values that need to be handled
# ------------------------------------------------------------
df = pd.read_csv("02_data_cleaning/raw_employees.csv")


# ------------------------------------------------------------
# Detect missing values
# isnull() returns:
# True  -> value is missing
# False -> value is present
# ------------------------------------------------------------
print(df.isnull())


# ------------------------------------------------------------
# Count how many missing values exist in each column
# This helps decide which columns need cleaning
# ------------------------------------------------------------
print(df.isnull().sum())


# ------------------------------------------------------------
# Handling missing values
# ------------------------------------------------------------

# Option 1: Drop columns or rows with missing values
# Use this only if the missing data is not important
# axis = 0 -> drop rows
# axis = 1 -> drop columns

# df.dropna(axis=1, inplace=True)
# print(df)


# Option 2: Replace missing values with a fixed value
# This is a simple approach but may affect data quality

# df.fillna(0, inplace=True)
# print(df)


# Option 3: Replace missing values with a calculated value
# Here we use the mean salary to fill missing salary values
# This keeps the data more realistic than using 0

df["employee_salary"].fillna(df["employee_salary"].mean(), inplace=True)


# ------------------------------------------------------------
# Display the cleaned dataset
# ------------------------------------------------------------
print(df)
