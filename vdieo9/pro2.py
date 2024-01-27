
# Write a Python program to check if an integer (x) is the power of another integer (y). Prompt the user to input both integers.
# Input: 16, 2
# Output: 4 ** 2 = 16


x = int(input("Enter a number x: "))
y = int(input(f"Enter a number y to test if x which is {x} is a power of y: "))

found = False

for k in range(2, x//2): #number like 1, 3, will result false anyway so we iterate from (2,x//2) to skip these trivial cases.
    if y ** k == x: #if the current value is a power
        print(f"{y} ** {k} = {x}") #formated printing
        found = True # set the boolean to true
        break
else:
    print(f'{x} is not the power of {y}') # this will run if y is not a power