# now detecting missing data

# first identify where data is missing
# isnull()  return True False

# true means yes the value is missing
# false means no the value is not missing

import pandas as pd

df = pd.read_csv("02_data_cleaning/raw_employees.csv")

print(df.isnull())

# to check how mnay value missing ----- return the count of missing values
print(df.isnull().sum())

# handling missing values

# we can remove whole colum or rows who has missing values ---- only in the case we dont need them

# df.dropna(axis = 1, inplace = True)

# # axis = 0 means row and axis = 1 means colm
# print(df)

# if we need the rows or colnm of missing values we add some values in place of them

# df.fillna(0,inplace=True)  # add the default value zero
# print(df)

# but if we want to add some calculated value in place of missing value (will use mean() of that colmn)

# 1st pic up the colm
df['employee_salary'].fillna(df['employee_salary'].mean(), inplace=True)
print(df)



