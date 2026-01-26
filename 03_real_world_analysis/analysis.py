import pandas as pd
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)

df = pd.read_csv("03_real_world_analysis/dataset/ddos.csv")


# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.head())

# print(df.isnull())
# print(df.isnull().sum())

duplicated_count = df.duplicated().sum()
print("Duplicated rows:", duplicated_count)

# The dataset contains a large number of duplicate rows.
# This is common in network traffic datasets due to repeated flows or logging behavior.

print("Rows before removing duplicates:",df.shape[0])

df = df.drop_duplicates()
print("Rows after removing duplicates:", df.shape[0])



"""What are “weird values”?

# Values that don’t make sense in real life, for example:
# Negative packet sizes
# Zero duration flows
# Negative bytes or packets
# Ports outside valid range (0–65535)"""
# Check summary stats to spot weird values
# print(df.describe())
print(
    (df[" Flow Duration"] < 0).sum()
)  # this is only to check if flow duration contain more negative values


# checking if any other colum have negative values
numeric_cols = df.select_dtypes(include="number")
# negative_counts = (numeric_cols < 0).sum()  # it counts all the colmuns negative values 
# print(negative_counts[negative_counts > 0])  #it print only the colmn that have neagtive values

df[numeric_cols.columns] = df[numeric_cols.columns].clip(lower=0)# It replaces all negative values in numeric columns with 0
print(df.describe())


# Attack vs Normal analysis
print(df[" Label"].value_counts()) 


#compare traffic behaviour between benign and attack flows

grouped_stats = df.groupby(" Label").mean()
print(grouped_stats)


grouped_stats.to_csv(
    "03_real_world_analysis/outputs/attack_vs_benign_means.csv"
)

df.to_csv(
    "03_real_world_analysis/outputs/cleaned_ddos.csv",
    index=False
)