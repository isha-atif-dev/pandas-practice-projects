# merging
import pandas as pd

df1 = pd.DataFrame(
    {
        "employee_id": [1, 2, 3, 4, 5],
        "employee_name": ["Asad", "Sara", "Bilal", "Soniya", "Ali"],
        "employee_age": [23, 45, 32, 32, 23],
    }
)
df2 = pd.DataFrame(
    {
        "employee_id": [1, 2, 3, 4, 6],
        "employee_salary": [60000, 34500, 56000, 30000, 20000],
    }
)

# merged = pd.merge(df1, df2, on="employee_id", how="outer")
# print(merged)

# inner
# outer
# left
# right
# cross

df3 = pd.DataFrame(
    {
        "employee_id": [1, 2, 3, 4, 5],
        "employee_name": ["Asad", "Sara", "Bilal", "Soniya", "Ali"],
        "employee_age": [23, 45, 32, 32, 23]
    }
)
df4 = pd.DataFrame({
        "employee_id": [6,7,8,9,10],
        "employee_name": ["Asaduulah", "Hana", "Ahmed", "Soni", "Aliwala"],
        "employee_age": [23, 45, 32, 32, 23]
})
# concatenation
concatenate = pd.concat([df3,df4],axis=0,ignore_index=True)
print(concatenate)