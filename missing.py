# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 16:30:25 2016

@author: Administrator
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import Imputer

s = pd.Series([1,2,3,np.NAN,5,6,None])

imp = Imputer(missing_values='NaN', strategy='mean',axis=0)

imp.fit([1, 2, 3, 4, 5, 6, 7])

x = pd.Series(imp.transform(s).tolist()[0])

print(s.isnull())
print()
print(s[s.isnull()])
print()
print(s.fillna(int(s.mean())))
print()
print(s.dropna())
print()
print(x)
