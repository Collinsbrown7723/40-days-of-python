l1 = list()
#print(dir(l1))
#print(help(l1.append))
#adding to list: append(), extend(), insert()

l1.append(2)
#(1)   l1.append(2,3) erro append takes exactly on argument
l1.append([2,3])

#(2)   extend takes an iteral
l1.extend([2,3,4,2,2,1,3,4,2])
l1.extend("hello")
 
#(3) insert method at given index
year = [2020,2022,2023]
year.insert(1,2021)
year.insert(len(year),2024)
print(year)
year.insert(-1,2025) # [2020, 2021, 2022, 2023, 2025, 2024]
print(year)
# clearing a list

year.clear()
print(year)

l1.pop() # removes the last value on the list

x = l1.pop() # it returs the value that can be stored to a varriable
print(x)
#.pop(1000) #out of range erro
print(l1)
print(l1.remove(2)) #it will remove the first instance of the argument

# use a while to remove all occurences
print(l1) 

while 1 in l1:
    l1.remove(1)
print(l1)

# list methods part 2
print("#" * 20 + " list method2 " + 20 * "#")

#list.index()

names = ["john","ben","paul","john"]
print(names.index("ben")) # will raise a valuerro in values doesnt exit

#list.count() it return the number of time a value appear in a list

letter = list("asdfghjhfgdsasasaASASFFDASDSSAaaaaa")
print(letter.count("a"))

# in operator

print("a" in letter)

#list.reverse

l2 = [1,2,"3",0.01]
l2.reverse()
print(l2)

# list.sort() and list.sorted()
ages = [23,42,12,4434,12,43,12,31,12,44,22,1,1,1]

sorted_list = sorted(ages)
print(f"sorted list{sorted_list}")
print(f"age is stil the same{ages}")

#sort()

n = ages.sort()
print(n) # returns none
print(f"age are affected by the .sort(){ages}")
m = ages.sort(reverse=True)
print(m)

# max() min()

print(ages)
print(max(ages))
print(min(ages))
print(sum(ages))