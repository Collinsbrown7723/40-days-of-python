import csv

# with open(" people.csv","a") as f:
#     writer = csv.writer(f)
#     data = (5,"collins","Ghana")
#     writer.writerow(data)

with open("number.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["x","x**2","x**3","x**4"])
    for x in range(1,101):
        writer.writerow([x,x**2,x**3,x**4])