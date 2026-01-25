# pandas interplolation

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

# df["employee_salary"] = df["employee_salary"].interpolate(method="linear")
# print(df)


# its has different methods like linear, time , and palanomial etc
# its disadvantage is that you cant work with categorical data like name, ids etc


# now sorting and agregation


# sorting data in 1 colmn
# df.sort_values(by= "colmen name ", true/false, inplace = True)
# here true false means in ascending or decending?

# df.sort_values(by="employee_name", ascending=True, inplace=True)
# # print(df)

# # agregation ___summary statistics

# avg_salary = df["employee_salary"].mean()
# sum = df["employee_salary"].sum()
# min = df["employee_salary"].min()
# max = df["employee_salary"].max()
# print(avg_salary)
# print(sum)
# print(min)
# print(max)


# # now grouping 

# grouped = df.groupby('employee_age')['employee_salary'].sum()
# print(grouped)


# # but if you want to group multiple colnms
# # grouped = df.groupby(['employee_age','employee_name'])['employee_salary'].sum()



