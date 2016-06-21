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

data = list(zip(map(int, root.xpath('Record/Number')),
           map(bool, map(util.strtobool, map(str, root.xpath('Record/Boolean'))))))

df = pd.DataFrame(data, columns=('Number', 'Boolean'),
                  index=map(str, root.xpath('Record/String')))
                  
print(df)    
print(type(df.ix['First']['Number']))
print(type(df.ix['First']['Boolean']))