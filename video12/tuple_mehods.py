#a tuple have only two methods tuple.index() and tuple.count()
t1 = (2,3,5,3,5,3)
x = t1.index(2)
#print(f"index at{x}") # will return an erro if value not in tuple
#x = t1.index(200)
# to avoid this

x = 3

if x in t1:
    i = t1.index(x)
    print(f"x in at index{i}")
else:
    print(f"{x} not in tuple")
    
#   count

n = t1.count("xx")
print(100 in t1)
# len() sum() max() min() sorted()
print(len(t1),sum(t1),min(t1),sorted(t1))
print(sorted(t1, reverse=True))