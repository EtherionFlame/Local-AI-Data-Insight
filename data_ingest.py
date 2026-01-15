import pandas as pd


df = pd.read_csv('Sample - Superstore.csv', encoding='windows-1252')

print(df.head())
print(df.dtypes)