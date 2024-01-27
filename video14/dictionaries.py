person = {"name":"john","age":40,"fav_movie":None,"alive":True}
#list set and dicts are immuterble and are not allowes as keys
# someone = {set("x"):"boy"} Erro
# tuples are allow because they are muterble
someone = {(2,3,5):"someperson"}
# print(type(person))
# d1 = dict()
# d2 = {}
# key = (2,3,5)
# print(someone[key])
print(len(person))

person["name"] = "collins"
print(person)
person["age"] = 23
 #    Erro
# a = person["agee"]
# print(a)
val = person.get("name","name doest exit")
print(val,person)

# pop method remvose the key

val2 = person.pop("age")
print(val2,person)

#popitem it will return the last value

val2 = person.popitem()
print(val2,person)

# to remove an item completely
# use the del 

del person["fav_movie"]
print(person)
#it raise an exception if the key doest exit in the dictionary
# del person["fav_spell"]
# print(person)

germany = {
    "city":["Hamburg","Berlin","Munich"],
    "info":{"population":80000,"people":["naruto","Einstein","Gause"]}
}

print(germany["info"]["people"][2])

countries = [
    {
    "city":["Hamburg","Berlin","Munich"],
    "info":{"population":80000,"people":["naruto","Einstein","Gause"]}
},
    {
    "city":["Ghana","Accra","Sunyani"],
    "info":{"population":8000,"people":["mark","flag","Gause"]}
}
]

print(countries[1]["info"]["people"][1])

#dictionary operations
# dict.key() and dict,value() and dict.items

d1 = {"name":"collins","age":23,"fav_languege":"python"}
val = d1.keys()
bal = d1.values()

print(f"keys in list {val},\nvalues {bal}")

nal = d1.items()# returns a list with all of the key and values
#being tuples
print(nal)

d2 = {10:"a",20:"x",30:"y"}
v = d2.values()
d2[10] = "x"
print(v)

print(20*"#")

print("name" in d1.keys())
print(("age",23) in d1.items())
d1 = {10:"c",20:"a"}
d2 = {20:"c",80:"c"}
k1 = d1.keys()
k2 = d2.keys()
print(k1 & k2)
print(k1 | k2)

# iteration over a dictionary
 #these work the same
persons = {"name":"collins","age":23,"fav_languege":"python"}
for person in persons:
    print(f"keys are {person}")
for person in persons.keys():
    print(f"keys are {person}")
    
# for the values

for person in persons.values():
    print(f"values are {person}")
    