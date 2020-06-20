import numpy as np
import pandas as pd

from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
df['W']
type(df['W'])

df['new'] = df['W'] + df['Y']
df

df.drop('new',axis = 1)
df

# inplace is used to permanently remove the changes to the DataFrame
df.drop('new',axis = 1,inplace = True)
df

df.drop('E')
df


# selecting rows
df.loc['A']
df.iloc[0]
df.loc['B','Y']
df.loc[['A','B'],['W','Y']]
