import numpy as np
import  pandas as pd

d = {'A':[1,np.nan,2],'B':[3,np.nan,np.nan],'C':[4,5,6]}
df = pd.DataFrame(d)
df

df.dropna()
df.dropna(axis = 1)
df.dropna(thresh = 2,axis = 1)

df['A'].fillna(value = df['A'].mean())
