# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 10:17:54 2016

@author: Administrator
"""

from lxml import objectify
import pandas as pd

xml = objectify.parse(open('XMLData2.xml'))
root = xml.getroot()

df = pd.DataFrame(columns=('Number','String','Boolean'))

for i in range(0,4):
    Obj = root.getchildren()[i].getchildren()
    row = dict(zip(['Number', 'String', 'Boolean'],
                   [Obj[0].text, Obj[1].text, Obj[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    df = df.append(row_s)

search = pd.DataFrame.duplicated(df)    
print(df)
print(search[search == True])

print(df.drop_duplicates())