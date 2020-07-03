import numpy as np
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

df['Special Power'] = df['Sp. Atk'] + df['Sp. Def'] # adding a new column
df.head()
df.drop(columns=['Sp. Atk', 'Sp. Def'])
df.head()
df.drop(columns='Special Power',inplace=True) # add inplace=True to make the change permanent
df.head()
df['Total Power'] = df.iloc[:,4:10].sum(axis = 1) # adding a new column using iloc
df.head()

df.insert(9,'Special Power', (df['Sp. Atk'] + df['Sp. Def'])) #add column at any position
# df.drop(columns='Special Power',inplace=True) # add inplace=True to make the change permanent
# df.head()
df.insert(9,'Special Power',df.iloc[:,7:9].sum(axis = 1))
# df.drop(columns='Special Power',inplace=True) # add inplace=True to make the change permanent
# df.head()
df.set_index('Name',inplace=True)
df.drop(['Bulbasaur','Ivysaur','Venusaur'])

df_new = pd.DataFrame({'Name':['Raj','Mia','Sree'],'Age': [20,22,24],'Place': ['KL','MH','UP']})
df_new
index_ = pd.date_range(start='2020-01-01',periods=3,freq='M')
df_new.index = index_
df_new
df_trunc = df_new.truncate(after='20200229') #Truncate DataFrame
df_trunc
df_trunc = df_new.truncate(before ='20200229')
df_trunc

df_iter = pd.DataFrame( {'name':["aparna", "pankaj", "sudhir", "geeku"],
                         'degree': ["MBA", "BCA", "M.Tech", "MBA"],
                         'score':[90, 40, 80, 98] } )
df_iter
for i, j in df_iter.iterrows(): #iterating over rows
    print(j,'\n')

#Handling missing data with pandas
df_null = pd.DataFrame( {'First':[100, 90, np.nan, 95],
        'Second': [30, 45, 56, np.nan],
        'Third':[np.nan, 40, 80, np.nan]} )
df_null
df_null.isnull() #checking for missing valiues using isnull()
bool_Series = pd.isnull(df_null['Third'])
bool_Series
df_null[bool_Series] #use ~ for not null values

df_null.notnull() #check using notnull
# In order to fill null values in a datasets, we use fillna() function
df_null.fillna(method='ffill')
df_null.fillna(method='bfill')


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
