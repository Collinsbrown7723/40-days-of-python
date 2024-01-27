import openpyxl
from openpyxl.styles import *

# sales3.xlsx -> https://drive.google.com/open?id=1a5iJfQORxz8OROT15m-bzeY2gNd26OlA
wb = openpyxl.load_workbook('sales3.xlsx')

sheet = wb.active


font = Font(name='Tahoma', size=16, color=colors.RED, bold=True, italic=False, strike=False)
cell_b6 = sheet['B6']
cell_b6.font = font

cell_c6 = sheet['c6']
cell_c6.font = font


wb.save('sales3.xlsx')