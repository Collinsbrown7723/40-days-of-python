# x = 10 #global variable
# y = 20
# def myFuction():
#     #x = 5 #local variable
#     global x # can use the global expression to make your x global
#     x +=1
#     print(f"x inside the function {x}")
#     return x
# myFuction()
# print(f"x outside the function {x}")

# def function2():
#     print(y)#python will look for it the global variable 
#     #if not found it will check  the builed in varilble

# function2()

# print(len("abc")) #3

# def len(x):
#     print(x)
# del len
# print(len("adsffsds"))

numbers = [1,2,0,4]
x = 10
def theFunction(numbers,x):
    numbers.append(9)
    x += 1
    numbers = [2,3]#this will not change the global variable
    print(f"x inside the function {x}")
theFunction(numbers,x)
print(f"x outside the function {x}\nnumbers now {numbers}")

# Global variable x
x = 10

def increment():
    global x    # this is the global variable x, not a local copy
    x += 1      # incrementing the global variable x

# Calling the function
increment()

# Printing the value of x after calling the function (x is 11)
print(x)