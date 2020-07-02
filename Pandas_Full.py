import pandas as pd
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

df.iloc[0,0] = 10
df.iloc[0,0]
df.iloc[0,0] = 1

#to iterate through the rows
for index, row in df.iterrows():
    if row['Type 1'] == 'Fire':
        print(row['Name'])

df.loc[df['Type 1'] == 'Fire']

#describing the dataset
df.describe()

#Sorting dataset
df.sort_values('Name')
df.sort_values('Name',ascending=False)
df.sort_values(['Name','Attack','Defense'],ascending=False)
df.sort_values(['Name','Attack','Defense'],ascending=[True,False,True])
df.sort_values(['Name','Attack','Defense'],ascending=[1,0,0]) #1 = True and 0 = False

#Operation on dataset

df['Special Power'] = df['Sp. Atk'] + df['Sp. Def']
df.head()
df.drop(columns=['Sp. Atk', 'Sp. Def'])
df.head()
df.drop(columns='Special Attack',inplace=True) # add inplace=True to make the change permanent
df.head()
df['Total Power'] = df.iloc[:,4:10].sum(axis = 1)
df.head()

#Filtering data
df.head()
df.loc[(df['Type 1'] == 'Fire') & (df['Legendary'] == True)]
df.loc[(df['Type 1'] == 'Water') & (df['Legendary'] == True) & (df['Total Power'] >= 600)]
gen6_legends =  df.loc[(df['Legendary'] == True) & (df['Generation'] >= 6)]
gen6_legends = gen6_legends.reset_index(drop = True)
gen6_legends

df.loc[df['Name'].str.contains('Mega')]
df.loc[~df['Name'].str.contains('Mega')]

#conditional Changes
df["Total Power"].max()
df.loc[df['Total Power'] > 700, ['Legendary','Generation']] = '# TEMP: '
df[df["Total Power"] >700]
df.loc[df['Total Power'] > 700, ['Legendary','Generation']] = ['Temp1','Temp2']
df[df["Total Power"] >700]

#Aggregate
df.head()
df.groupby(['Type 1']).mean().sort_values('Attack',ascending=False)
df['Count'] = 1
df.groupby(by=['Type 1','Type 2']).count()['Count']

#Saving dataset

df.to_csv('modified.csv', index=False)
df.to_excel('modifie.xlsx', index = False)
df.to_csv('modified.txt', index=False, sep ='\t')
