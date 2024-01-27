import openpyxl
import csv






def csv2excel(people3csv, teachersxlsx):
    people = list()
    with open("people3.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            people.append(row)
            
    wb =  openpyxl.load_workbook("teachers.xlsx")

    sheet = wb.active
    for row in people:
        sheet.append(row)
    
    wb.save("teachers.xlsx")

csv2excel("people.xlsx","people.csv")