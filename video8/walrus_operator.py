#name := expression
#print(y = 6) //this will return an erro because the  = operator do not return anything
print(x:=2*9) # return a value and also store to var 'x'
print(f"the value of x is {x}")

value = input("Enter something:")
while value != "":
    print(f"youve entered{value}")
    value = input("Enter something")
    
#better way 

while(value:=input("Enter something"))!= "":
    print(f"sorry try again")
    
#######################################
data = input("Enter your name:")
if len(data)<0:
    print(f"your name has {len(data)}")
else:
    print("Your name cant be empty")
#########################################
data = input("Enter a name")
if(n := len(data) < 0):
    print(f"your name is {n} chars long")
else:
    print("Your name cant be empty")