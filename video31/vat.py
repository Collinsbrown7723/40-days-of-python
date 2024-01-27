import openpyxl

wb = openpyxl.load_workbook("sales.xlsx")
# read the entire content in a list
sheet = wb["COMPANY SALES"]
items = list()
for row in sheet.values:
    items.append(row)
    
# calculating the vat values
vat = list()
for row in items[1:]:
    element = (row[0], row[1] * 0.15)
    vat.append(element)
# add a new sheet called vat
wb.create_sheet('VAT')
sheet = wb['VAT']

# add a header (column names)
sheet['A1'] = 'Year'
sheet['B1'] = 'VAT'

# appending to the new sheet
for row in vat:
    sheet.append(row)
wb.save("sale_and_vat.xlsx")