# # x = set()
# x = set()
# s1 = {1,"a",3,2,1,5,0,"a",True}
# print(x,s1)
# s1.add((10,20))
# print(s1)
# s1.remove("a")
# print(s1)
# #sets are mutable
# l1 = [2,3]#sample list

#s1.add(l1)#TypeError: unhashable type: 'list'
# #cant add unmutable data to sets
# #print(s1[0])# 'set' object is not subscriptable
# s3 = {}
# print(type(s3)) #s3 is not a set but dictionary

# # str => set

# s4 = set("hello python")
# print(s4)
# # from tuple
# s5 = set((2,3,"a",True))
# print(s5)
# # from list
# l2 = [2,7,7,7,6,6,7,7,7,7,7,7,3,3,5,6,7]
# s6 = set(l2)
# print(s6)
# mac = ["e0:9d:31:7d:f2:2c","e0:9d:31:7d:f2:2c","e0:9d:31:7d:f2:2c",
#        "e0:9d:31:7d:f2:2c","e0:9d:31:7d:f2:2c","e0:9d:31:7d:f2:2i"]
# mac_addresses = set(mac)
# mac_addresses_list = list(set(mac_addresses))
# print(mac_addresses,len(mac_addresses),type(mac_addresses_list))
# print("e0:9d:31:7d:f2:2c" in mac) # True
# for _ in mac_addresses:
#     print(_)

# set1 = {1,2,3}
# set2 = {1,3,2}

# print(set1 is set2)
# print(set1 == set2)

# l1 = ([2,3,4])
# l2 = ([2,4,3])

# print(l1 is l2)
# print(l1 == l2)



# set methods set.add(x) set.remove(x) set.discard(x)

# s1 = {1,5,7,89,"helloo"}
# s1.add(4)
# s1.add(1)# does nothing

# s1.remove(1)
# #s1.remove(5) Erro

# s1.discard(5)
# s1.discard(6)# does nothing
# print(s1)
# val = s1.pop()# remove random element from a set
# print(val)
 
# set1 = set("abc")
# set2 = set1
# set2.add("y")
# set1.add("q")
# print(set1 ,set2)
# set1.clear()
# print(set1, set2) # they are forever connected to the place in memory

# set4 = set([2,3,4])
# print(set4)
# set5 = set4.copy()

# print(set5,type(set5))
# print(set4 == set5)
# set5.add("x")
# print(set4 , set5) # after .copy they become indepent of each other


# set method part 2

set1 = {1,2,5}
set2 = {5,7,9}
set3 = set1.intersection(set2)
set4 = set1 & set2
print(set3)
print(set4)

# defference
set1 = {1,2,5}
set2 = {5,7,9}
#two ways
set3 = set1.difference(set2)
set_3 = set1 - set2
#two ways
set4 = set2.difference(set1)
set_4 = set2 - set1
print(set3, set_3)
print(set4, set_4)

# symmetric (^) commond elements are excluded
set1 = {1,2,5}
set2 = {5,7,9}


set4 = set1.symmetric_difference(set2)
set5 = set1 ^ set2
print(set4,set5)

# union commond stuff
set1 = {1,2,5}
set2 = {5,7,9}

set4 = set1.union(set2)
set5 = set1 | set2

print(set4, set5)

# set.isdisjoint()
set7 = set(["x","y"])
print(set1.isdisjoint(set2)) # false because of element 5
print(set1.isdisjoint(set7))

# < ,> ,<= ,>= ,= ,== containment testing
# returns a boolean literal


