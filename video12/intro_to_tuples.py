t1 = tuple()
t2 = ()
print(type(t1),type(t2))
t1 = (1,"hello",0.2,True)
print(t1)
t4 = (10)#is it a tuple // to declear a tuple with only one element use a , (x,)
t5 = (10,)
print(type(t4),type(t5))#<class 'int'> <class 'tuple'>
t5 = 2,10,"python",True
print(type(t5))#<class 'tuple'> is not common but is possible to create a tuple without()
t6 = tuple([2,"hee"])
t7 = tuple("hello")
print(t6,f"----{t7}")
l1 = list(t1)
print(type(l1))# <class 'list'> get list from tuples
#
#
#               index selection x[0] for first x[-1] for last
print(t1[0],t1[-1])
#t1[2] = "x" 
#   t1[2] = "x" 
# TypeError: 'tuple' object does not support item assignment

# tuple are immuterble
