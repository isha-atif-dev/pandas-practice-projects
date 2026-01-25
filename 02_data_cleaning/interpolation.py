# ------------------------------------------------------------
# interpolation.py
# This script demonstrates how to fill missing numeric values
# using pandas interpolation.
# ------------------------------------------------------------

import pandas as pd

# ------------------------------------------------------------
# Load the raw dataset
# The dataset contains missing values in numeric columns
# ------------------------------------------------------------
df = pd.read_csv("02_data_cleaning/raw_employees.csv")
# Pandas interplolation

# Filling missing values by estimating them using nearby values.

# Instead of:
# deleting missing data
# or filling with a fixed number (like 0 or mean)

# purpose
# 1. to preserve data integrity
# 2. for smooth trends
# 3. avoid data lose

# it has alot of methods
# df.interpolate(method="linear", axis=0, inplace=True)

df["employee_salary"] = df["employee_salary"].interpolate(method="linear")
print(df)


# ------------------------------------------------------------
# Notes:
# - Interpolation should only be used on numeric columns
# - It does not work for categorical data (names, IDs, labels)
# - Other methods exist: linear, time, polynomial, etc.
# ------------------------------------------------------------