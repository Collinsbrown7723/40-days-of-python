my_tuple = (1,0.3,"python",False,(30,40))

t1 = my_tuple + tuple("xy")
print(t1)
t2 = tuple([2,"hell"]*6)
# print(t2)
# print(my_tuple[0:4])
# print(my_tuple[:4])
# print(my_tuple[3:])
# print(my_tuple[::])
# print(my_tuple[::2])# step by 2
# print(my_tuple[::-1]) # reverse
# print(my_tuple[-1:0:-1])

spells = ("expecto petronium","lengavio leviosor","expelliyamus")
for spell in spells:
    print(f"harry potter cast {spell}")
print("expelliyamus" in spells)
print("abagdabra" in spells) # false
print("python" not in spells) # True