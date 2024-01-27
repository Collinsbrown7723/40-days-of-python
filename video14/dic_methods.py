person = {"name":"collins brown","location":"Ghana"}
me = person
print(id(me) == id(person))
# dict.copy()
another_person = person.copy()

another_person["name"] = "shalom"
another_person["location"] = "plains"
print(f"me {me}")
print(f"another {another_person}")

print("#"*20)
#dict.update()
countries = {"ghana":"gh","us":"united state","de":"germany"}
countries.update({"ng":"nigeria"})
print(countries)
countries.clear()
print(countries)