import openpyxl
# sales2.xlsx -> https://drive.google.com/open?id=1Yw0j7v49-Mcrve6vN3h6yLTMxkSmdqqx
wb = openpyxl.load_workbook('Company.xlsx')
sheet = wb["COMPANY SALES"]
# sheet = wb.active


cell = sheet['B6']
cell.value = '=sum(B2:B5)'


cell = sheet['C6']

cell.value = 'Total Sales'

wb.save('sales3.xlsx')