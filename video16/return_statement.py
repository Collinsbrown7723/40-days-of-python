def func1(x,y):
    return x + y
def func2(x,y):
    print(x + y)
n = func1(10,23)
print(n)
func2(3,2)
nill = func2(2,3)
print(nill)

def func3(x,y):
    return (x + y)
    print("this will never run")
def func4(x,y):
    x = x**x
    y = y**y
    return x,y, y-10 #add as many as you want
this_is_a_tuple = func4(2,3)
print(type(this_is_a_tuple),this_is_a_tuple)

#we have three values returning from the fuction
#we can do this
a,b,c = func4(2,8)
print(a,b,c)
#that is if you know how many values will be returned
#use this if you dont 
#this is called unpacking
x,*y = func4(90,2)
print(type(x),type(y))