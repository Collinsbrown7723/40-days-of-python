##############################
## The sys module
##############################

## Importing the module
import sys

## Returns the version of the Python interpreter
sys.version

## Other info about the interpreter
sys.implementation

## Returns the platform (linux, win32 or mac)
sys.platform

## Returns the PATH (directories where it searches for modules)
sys.path

my_list = list(range(100))
sys.getsizeof(my_list)      # returns the size of the list in memory


## Redirecting output to a file instead of stdout (console)

x = sys.stdout

with open("out.txt","w")as sys.stdout:
    print("hell owepr")
    
sys.stdout = x