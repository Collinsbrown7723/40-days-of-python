#loops and ranges

s = 0
for n in range(101):
    s += n
print(f"sum = {s}")

for _ in  range(10): #the underscore holds the termporary variable
    print("Do somthing", _) 
import random
names = ['collins','mark','linus','elvis','brown','name','hewhomustnotbenamed']
for _ in range(3):
    print(f"chosing the winner .round {_}")
    winner = random.choice(names)
    names.remove(winner)
    print(f"the winner is {winner}")