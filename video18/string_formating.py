s = "expecto petronium"
ip = "    192.222.1.20        " 
value = "$$$$$900909$$$"
# we use the dot notation to access the builed in python
#function
print(s.upper())
#string literals are immuterble so the python returns a new string 
low  = s.lower()
print(low)
print(s) #s remains the same
print(ip.strip()) #removes all spaces from beging and ending
print(value.strip("$")) # this will strip the doller sign away
print(value.replace("$","@")) #this will replace the "$" with "@"
counting = "ha ha ha ha i am loard voldermold"
print(counting.count("ha")) # will return the number of occurences
clone = "Ha Ha Ha Ha i am loard voldermold"
print(clone.count("ha")) #case sense
#les fix that
add = "*"
print(clone.lower().count("ha")) # fun().fun() 
print(add.join(clone)) # adds the .fun() to the () 
clone = "Ha Ha Ha Ha i am loard voldermold"
#the .find() finds the first occurec of the arguments index
print(clone[clone.lower().find("ha"):2])
print("ha" in clone) #False
print("Ha" in clone) #True
print("ha" is not clone) # True
print("Ha" is not clone) #True 
print("Ha" not in clone)#False
print("ha" not in clone) #True