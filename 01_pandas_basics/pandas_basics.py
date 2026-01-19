import pandas as pd

df = pd.read_csv("basics-of-pandas/CsvData.csv")
# print(df.to_string(index=False))


# after manipulation hwo to save data in pandas

# how to create a dataframe using dict

# A DataFrame is a 2-dimensional data structure used to store and work with tabular data (rows + columns).


data = {
    "Name": ["Ali", "ahmed", "sufyan"],
    "Age": [23, 30, 21],
    "location": ["jhelum", "lahore", "isb"],
}

# df = pd.DataFrame(data)
# print(df)

# df.to_excel('data.xlsx',index=False)
df.to_json("data.json", index=False)


# how to read rows of dataframe like to understand about the data

# head(n)
# tail(n)


# how many colns ,rows
# what size
# what type of data store in each colm
# missing values
# mempory usage

# info()   give concise summary of your dataframe to ans above questions


df2 = pd.read_csv("basics-of-pandas/ddos.csv")
# print(df2.info())


# describe method

# print(df2.describe())


# now i want to know about how many no of colm and rows i have
# shape

# print(df2.shape)
# print(df2.columns)


# now selecting specific or 2 colum
subset = df2[[" Destination Port", " Flow Duration"]]
# print(subset)

# filter rows
# combine multiple conditions

age = df[(df["marks"] > 80) & (df["age"] < 23)]
print(age)
