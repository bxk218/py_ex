# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 16:52:37 2016

@author: Administrator
"""

import re

data1 = 'My phone number is: 800-555-1212.'
data2 = '800-555-1234 is my phone number.'

pattern = re.compile(r'(\d{3}) - (\d{3}) - (\d{4})')

dmatch1 = pattern.search(data1).groups()
dmatch2 = pattern.search(data2).groups()

print(dmatch1)
print(dmatch2)
