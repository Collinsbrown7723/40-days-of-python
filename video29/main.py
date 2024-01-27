friend = {"collins":[20,"ghana"],"mark":[30,"ghana"]}
print(type(friend))
with open("friends.txt","w") as f:
    f.write(repr(friend))
with open("friends.txt","r")as f:
    data = f.read()
print(data)
print(type(dict(data))) ## it seems i can do this less fine another way