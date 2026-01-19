import pandas as pd

"""
01_pandas_basics
This script demonstrates fundamental pandas operations including:
- loading tabular data from CSV
- basic data exploration and inspection
- summary statistics
- column selection and row filtering
- manual DataFrame creation
- saving processed outputs to files

These steps reflect the initial phase of a real-world data workflow.
"""

# -------------------------------------------------------------------
# 1. Load dataset from CSV
# This simulates reading raw data exported from a database or system
# -------------------------------------------------------------------
df = pd.read_csv('01_pandas_basics/CsvData.csv')


# -------------------------------------------------------------------
# 2. Explore the dataset structure and content
# Used to understand data shape, columns, data types, and missing values
# -------------------------------------------------------------------
print(df.head())      # Preview first few rows
print(df.tail())      # Preview last few rows
print(df.shape)       # Returns (rows, columns)
print(df.columns)     # Column names
print(df.info())      # Data types, non-null counts, memory usage


# -------------------------------------------------------------------
# 3. Summary statistics
# Provides quick insight into numeric distributions, averages, and ranges
# Useful for detecting anomalies or unexpected values
# -------------------------------------------------------------------
summary_of_data = df.describe()
print(summary_of_data)


# -------------------------------------------------------------------
# 4. Column selection
# Extracting only relevant features for analysis or reporting
# -------------------------------------------------------------------
subset = df[['name', 'marks']]
print(subset)


# -------------------------------------------------------------------
# 5. Row filtering using multiple conditions
# Represents real-world rule-based filtering (e.g. eligibility checks)
# -------------------------------------------------------------------
student_marks = df[
    (df['marks'] > 50) &
    (df['marks'] < 70) &
    (df['age'] < 24)
]

print(student_marks)


# -------------------------------------------------------------------
# 6. Creating a DataFrame manually
# Common when generating reports, test data, or derived results
# -------------------------------------------------------------------
data = {
    'employee_id': [1, 2, 3, 4, 5],
    'employee_name': ['Asad', 'Sara', 'Bilal', 'Soniya', 'Ali'],
    'employee_salary': [60000, 120000, 56000, 30000, 200000]
}

df2 = pd.DataFrame(data)
print(df2)


# -------------------------------------------------------------------
# 7. Saving outputs
# Persisting processed data for downstream tasks or sharing
# -------------------------------------------------------------------
df2.to_csv('outputs/new_dataframe.csv', index=False)
df2.to_json('outputs/new_dataframe.json', index=False)
df2.to_excel('outputs/new_dataframe.xlsx', index=False)
