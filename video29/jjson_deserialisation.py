import json

with open("friends.json","rt") as f:
    obj1 = json.load(f)
print(obj1)

json_str = """{
    "collins": [
        20,
        "ghana"
    ],
    "mark": [
        30,
        "ghana"
    ]
}"""

obj2 = json.loads(json_str)
print(obj2)