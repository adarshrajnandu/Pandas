import pandas as pd
print(pd)
df = pd.read_csv('pokemon_data.csv')

df.head()

#to read column names or headers
df.columns

#read columns
df['Name']
df['Name'][:10]
df[['Name','HP','Defense']]

#reading rows

df.loc[0]
df.iloc[0]
df.loc[0:5]
df.iloc[0:5]
df.loc[2,'Attack']
df.iloc[2,5]
