import openpyxl

wb = openpyxl.Workbook()

sales = {"2001":"1000","2002":"3000","2003":"9000","2004":"30023"}

sheet =  wb.active
sheet["A1"] = "year"
sheet["B1"] = "sales"
for k,v in sales.items():
    sheet.append((k,v))

wb.save("saved.xlsx")