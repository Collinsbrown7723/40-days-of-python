"""Challenge #2

Change the solution from the previous challenge and use : (colon) as the delimiter."""
people = [

['Dan', 34, 'Bucharest'],

['Andrei',21, 'London'],

['Maria', 45, 'Paris']

]
print(people)
print(type(people))

import csv
csv.register_dialect("commer",delimiter=":",lineterminator="\n")

with open("people.csv","a") as f:
    writer = csv.writer(f,dialect="commer")
    for x in people:
        writer.writerow(x)

with open("people.csv","r")as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)