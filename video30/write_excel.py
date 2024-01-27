import openpyxl

wb = openpyxl.load_workbook('store.xlsx')
name1 , name2 = wb.sheetnames
print(name1,name2)
#sheet = wb[name1]
sheet = wb.active
sheet = wb[name1]
# new_product = (11,"tablet",12,600,12*600)
# sheet.append(new_product)

for c,d,e in sheet["c2:e12"]:
    e.value = c.value * d.value
wb.save("store.xlsx")