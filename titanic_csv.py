# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 22:47:16 2016

@author: Byungtae
"""

import pandas as pd
titanic = pd.io.parsers.read_csv("Titanic.csv")
X = titanic[['Age']].values
print(X)
