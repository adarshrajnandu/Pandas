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

#conditional selection

df > 0
booldf = df > 0
df[booldf]
df[df>0]

df['W'] > 0
df[df['W']>0]
df[df['Z'] <0]
df[df['W']>0]['X']

# when series of boolean values are compared use '&' instead of 'and'
df[(df['W'] > 0) & (df['Y'] > 0)]

new_ind = 'CA NY WY OR CO'.split()
new_ind
df['States'] = new_ind
df.set_index('States')
df
df.set_index('States',inplace = True)
df


#Index levels

outside = 'G1 G1 G1 G2 G2 G2'.split()
inside = [1,2,3,1,2,3]
hier_index =  list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

outside
inside
hier_index
 df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
df
df.loc['G1']
df.loc['G1'].loc[1]
df.index.names = ['Groups','Nums']
df
df.loc['G2'].loc[2]['B']

#cross selection indexing

df.xs(1,level = 'Nums')
