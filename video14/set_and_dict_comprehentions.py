names = {"colinx","Mark","Jnr","LInux"}
name = {n.capitalize() for n in names}
print(name)

d1 = {"a":2, "b":5}
#d1 = {i*2:k*2 for i,k in d1.items()}
print(d1)
d3 = {i.capitalize() for i in d1.keys()}
print(d3)
d4 = {j*30 for j in d1.values()}
print(d4)


print(20*"#")

years = [2000,2001,2020]
revenu = [2093093,8280,332]
z = zip(years,revenu)
sales = list(z) # after unpacking a zip file the data in z is droped
print(sales)
my_sales = dict(zip(years,revenu))
print(my_sales , type(my_sales))
profit = [k*0.15 for k in my_sales.values()]
print(profit)
profit ={i:k*0.15 for i,k in my_sales.items()}
print(profit.values())