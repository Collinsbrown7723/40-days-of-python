import csv

# with open(" passwd.csv","r")as f:
#     reader = csv.reader(f,delimiter=":",lineterminator="\n")
#     for row in reader:
#         print(row)
# print(csv.list_dialects())

#when registering a dielet
csv.register_dialect("hashes",delimiter="#",lineterminator="\n")

with open(" items.csv") as f:
    reader =  csv.reader(f,dialect="hashes")
    for row in reader:
        print(row)

with open(" items.csv","a") as f:
    writer = csv.writer(f,dialect="hashes",lineterminator="\n")
    writer.writerow(("spoon",44,33))
