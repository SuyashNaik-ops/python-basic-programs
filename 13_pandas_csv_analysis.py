import pandas as pd

df = pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nStatistical summary:")
print(df.describe())

print("\nNumber of rows and columns:")
print(df.shape)

print("\nColumn names:")
print(df.columns)