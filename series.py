import numpy as np
import pandas as pa

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30}

pd.Series(data = my_data, index = labels)
pd.Series(arr,labels)
pd.Series(d)
