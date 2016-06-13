#! python3

import pandas as pd
xlsx = pd.ExcelFile("skimmed.xlsx")
trig_values = xlsx.parse('Skimmed data', index_col=None, na_values=['NA'])
print(trig_values)

'''
import openpyxl
from openpyxl.styles import Font, Color, Style, colors

print('Opening workbook...')
wb = openpyxl.load_workbook('skimmed.xlsx')
sheet = wb.get_sheet_by_name('Skimmed data')

print('Reading rows...')
for row in range(2, sheet.get_highest_row() + 1):
	if sheet2['A' + str(row)].value != sheet1['A' + str(row)].value :
		sheet2['A' + str(row)].style = Style(font=Font(color=Color(colors.BLUE)))
	if sheet2['B' + str(row)].value != sheet1['B' + str(row)].value :
		sheet2['B' + str(row)].style = Style(font=Font(color=Color(colors.BLUE)))
	if sheet2['C' + str(row)].value != sheet1['C' + str(row)].value :
		sheet2['C' + str(row)].style = Style(font=Font(color=Color(colors.BLUE)))

wb2.save('modified.xlsx')
print('Done.')
'''