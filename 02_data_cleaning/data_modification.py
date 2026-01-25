# ------------------------------------------------------------
# data_modification.py
# This script demonstrates how to modify an existing dataset by adding, updating, and removing columns and values using pandas.
# ------------------------------------------------------------

import pandas as pd

# ------------------------------------------------------------
# Load the dataset
# ------------------------------------------------------------
df = pd.read_csv("02_data_cleaning/raw_employees.csv")


# ------------------------------------------------------------e
# added a new column to the DataFrame
# ------------------------------------------------------------
new_colm_data = [
    85, 70, 89, 90, 87, 99, 98, 89, 87, 78,
    85, 70, 89, 90, 87, 99, 98, 89, 87, 78,
    85, 70, 89, 90, 87, 99, 98, 89, 87, 78,
    85, 70, 89, 90, 87, 99, 98, 89, 87, 78,
]

# Using insert() allows placing the column at a specific index
# Syntax: df.insert(column_index, column_name, column_data)
df.insert(4, "performance_score", new_colm_data)


# ------------------------------------------------------------
# Update a specific value using .loc
# This is commonly used for correcting incorrect or updated records
# ------------------------------------------------------------
df.loc[2, "employee_salary"] = 70000


# ------------------------------------------------------------
# Update values of an entire column
# This simulates recalculating or adjusting scores or metrics
# ------------------------------------------------------------
df["performance_score"] = df["performance_score"] + 1


# ------------------------------------------------------------
# Drop a column
# inplace=True modifies the original DataFrame
# ------------------------------------------------------------
df.drop(columns=["performance_score"], inplace=True)


# ------------------------------------------------------------
# Display the modified DataFrame
# ------------------------------------------------------------
print(df)

# ------------------------------------------------------------
# Note:
# Multiple columns can be dropped at once using:
# df.drop(columns=["col1", "col2"], inplace=True)
# ------------------------------------------------------------
