#range()
r = range(2,10) #start and stop
print(type(r))
print(r)
print(list(r))
r2 = range(10)# the generate statement will start from 0
r3 = range(1,20,3)#the third arguement is the step value
print(list(r3))#[1, 4, 7, 10, 13, 16, 19] by default the step is set to one
s = sum(range(0,1001))
print(s)
