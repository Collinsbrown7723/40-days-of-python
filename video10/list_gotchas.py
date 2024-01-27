l1 = [1,2,3,4]
l2 = l1
l2[0] = "x"
l2.append("hello")
print(f"l1 = {l1}")
print(f"l2 = {l2}")
print(id(l1))
print(id(l2))
# both l1 and l2 share the same  reference data
l1.remove("hello")
print(l2)
# to make a different list use the .copy() expression
l3 = l1.copy()
print(l3)
print(id(l3))
print(id(l1)) #both have different ids