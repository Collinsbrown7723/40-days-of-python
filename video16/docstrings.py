#Docstrings

def say_hello(name):
    """this function says hello """
    print(f"hello {name} , nice to meet yay")
say_hello("collins")

print(say_hello.__doc__)
print(help(say_hello))