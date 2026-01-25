# ------------------------------------------------------------
# merging_and_concat.py
# This script demonstrates how to combine multiple DataFrames
# using merge and concat operations in pandas.
# ------------------------------------------------------------

import pandas as pd


# ------------------------------------------------------------
# Create first DataFrame (basic employee details)
# ------------------------------------------------------------
df1 = pd.DataFrame(
    {
        "employee_id": [1, 2, 3, 4, 5],
        "employee_name": ["Asad", "Sara", "Bilal", "Soniya", "Ali"],
        "employee_age": [23, 45, 32, 32, 23],
    }
)


# ------------------------------------------------------------
# Create second DataFrame (salary information)
# This simulates data coming from a different source/system
# ------------------------------------------------------------
df2 = pd.DataFrame(
    {
        "employee_id": [1, 2, 3, 4, 6],
        "employee_salary": [60000, 34500, 56000, 30000, 20000],
    }
)


# ------------------------------------------------------------
# Merging DataFrames
# Merge combines DataFrames based on a common key (employee_id)
# ------------------------------------------------------------

# Example merge (commented for demonstration)
# merged = pd.merge(df1, df2, on="employee_id", how="outer")
# print(merged)

# Common merge types:
# inner -> only matching rows from both DataFrames
# outer -> all rows from both DataFrames
# left  -> all rows from left DataFrame
# right -> all rows from right DataFrame
# cross -> cartesian product


# ------------------------------------------------------------
# Create two DataFrames for concatenation
# Concatenation stacks DataFrames row-wise or column-wise
# ------------------------------------------------------------
df3 = pd.DataFrame(
    {
        "employee_id": [1, 2, 3, 4, 5],
        "employee_name": ["Asad", "Sara", "Bilal", "Soniya", "Ali"],
        "employee_age": [23, 45, 32, 32, 23],
    }
)

df4 = pd.DataFrame(
    {
        "employee_id": [6, 7, 8, 9, 10],
        "employee_name": ["Asaduulah", "Hana", "Ahmed", "Soni", "Aliwala"],
        "employee_age": [23, 45, 32, 32, 23],
    }
)


# ------------------------------------------------------------
# Concatenate DataFrames row-wise
# axis=0 stacks rows
# ignore_index=True resets the index
# ------------------------------------------------------------
concatenate = pd.concat([df3, df4], axis=0, ignore_index=True)

print(concatenate)