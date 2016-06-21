# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 10:17:54 2016

@author: Administrator
"""

from lxml import objectify
import pandas as pd
from distutils import util

xml = objectify.parse(open('XMLData.xml'))
root = xml.getroot()
df = pd.DataFrame(columns=('Number', 'Boolean'))
#df = pd.DataFrame(columns=('Number','String','Boolean'))

for i in range(0,4):
    Obj = root.getchildren()[i].getchildren()
    row = dict(zip(['Number', 'Boolean'],
                   [Obj[0].pyval, 
                    bool(util.strtobool(Obj[2].text))]))
    row_s = pd.Series(row)
    row_s.name = Obj[1].text
    df = df.append(row_s)

#search = pd.DataFrame.duplicated(df)
print(df)    
print(type(df.ix['First']['Number']))
print(type(df.ix['First']['Boolean']))