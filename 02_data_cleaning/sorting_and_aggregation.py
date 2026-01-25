# ------------------------------------------------------------
# sorting_and_aggregation.py
# This script demonstrates how to sort data and calculate
# summary statistics using pandas.
# ------------------------------------------------------------

import pandas as pd

# ------------------------------------------------------------
# Load the cleaned dataset
# ------------------------------------------------------------
df = pd.read_csv("02_data_cleaning/raw_employees.csv")


# ------------------------------------------------------------
# Sorting data
# Sorting helps organise data for analysis and reporting
# ------------------------------------------------------------

# Sort employees by name in ascending order
# ascending=True  -> A to Z
# ascending=False -> Z to A
df.sort_values(by="employee_name", ascending=True, inplace=True)

print(df)


# ------------------------------------------------------------
# Aggregation (summary statistics)
# Aggreg let us understand overall trends in numeric data
# ------------------------------------------------------------

avg_salary = df["employee_salary"].mean()   # Average salary
total_salary = df["employee_salary"].sum()  # Total salary
min_salary = df["employee_salary"].min()    # Lowest salary
max_salary = df["employee_salary"].max()    # Highest salary

print("Average salary:", avg_salary)
print("Total salary:", total_salary)
print("Minimum salary:", min_salary)
print("Maximum salary:", max_salary)


# ------------------------------------------------------------
# Grouping data
# Grouping is used to aggregate data based on categories
# ------------------------------------------------------------

# Total salary grouped by employee age
grouped = df.groupby("employee_age")["employee_salary"].sum()
print(grouped)


# ------------------------------------------------------------
# Note:
# Multiple columns can be used for grouping when needed
# Example:
# df.groupby(["employee_age", "employee_name"])["employee_salary"].sum()
# ------------------------------------------------------------
