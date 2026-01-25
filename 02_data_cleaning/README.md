# Data Cleaning with Pandas

This folder focuses on data cleaning and data modification techniques using pandas.
It demonstrates how raw or dirty datasets are prepared before analysis or modeling.

The scripts here cover common real-world data cleaning tasks that are frequently
used in data analysis and machine learning workflows.

---

## Files Overview

### data_modification.py
Demonstrates how to modify existing DataFrames.

Concepts covered:
- Adding new columns
- Inserting columns at a specific position
- Updating individual cell values using `.loc`
- Updating entire columns
- Dropping unnecessary columns
- Understanding the effect of `inplace=True`

---

### missing_data.py
Focuses on detecting and handling missing values.

Concepts covered:
- Detecting missing values using `isnull()`
- Counting missing values using `isnull().sum()`
- Removing missing data using `dropna`
- Filling missing values using `fillna`
- Replacing missing values with column mean

Why it matters:
- Real-world datasets often contain incomplete data
- Proper handling prevents incorrect analysis results

---

### interpolation.py
Demonstrates filling missing numeric values using interpolation.

Concepts covered:
- Understanding what interpolation is
- Filling missing values using nearby values
- Using linear interpolation
- Knowing when interpolation is appropriate

Why interpolation is used:
- Preserves data trends
- Avoids data loss
- Produces smoother results than fixed values

---

### sorting_and_aggregation.py
Covers sorting, aggregation, and grouping operations.

Concepts covered:
- Sorting data using `sort_values`
- Calculating summary statistics:
  - mean
  - sum
  - min
  - max
- Grouping data using `groupby`
- Aggregating grouped results

---

### merging_and_concatenation.py
Demonstrates combining multiple DataFrames.

Concepts covered:
- Merging DataFrames using `merge`
- Understanding join types:
  - inner
  - outer
  - left
  - right
- Concatenating DataFrames using `concat`

---

## Datasets Used
- Raw employee datasets containing missing and inconsistent values
- Used only for learning and practice purposes

---

## Purpose of This Folder
- Learn how to clean and prepare real-world data
- Understand common data issues and solutions
- Build strong pandas fundamentals for analysis and ML projects

---

## Status
Completed core pandas data cleaning concepts.