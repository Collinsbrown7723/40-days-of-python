def myFunction(x,y = 10,z = 3): #when you diffine posional args example y = 10
    #all following args must be asigned posional args z = 3
    print(f"x is {x} and y is {y} z to is {z}")
    print(x+y)
myFunction(10,y=10,z = 10)