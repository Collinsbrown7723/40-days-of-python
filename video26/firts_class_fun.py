def summ(number,fn):
    result = 0
    for n in range(1,number+1):
        result += fn(n)
    return result
def sqr(x):
    return x ** 2

result = summ(3,sqr)
print(result)

import math

result = summ(10,math.sqrt)
print(format(result,".5f"))

def compute(msg):
    if msg =="square":
        return sqr
    else:
        return math.sqrt
fun = compute("square")
print(fun(10))