# Write a Python script that draws the following pattern using for loops.

# *

# * *

# * * *

# * * * *

# * * * * *

# * * * *

# * * *

# * *

# *
count = 1
for i in range(11):
    if i < 5:
        print("x" * count) 
        count += 1
    elif i == 5:
        print("x" * count)
        count -= 1
    elif i > 5:
        print("x" * count)
        count -= 1
        
    
        
        