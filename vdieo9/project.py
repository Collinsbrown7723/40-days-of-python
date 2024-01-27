# Create a Python script that asks the user for a number and then prints out a list of all the divisors of each number
# less than the asked number.
x = 0

devisor = list()

x = int(input("Enter number"))

for _ in range(1,x):
    if x%_==0:
        devisor.append(_)
    else:
        continue
print(devisor)
print(len(devisor))
        
