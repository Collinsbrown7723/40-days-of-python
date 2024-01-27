#Given the string s1, write a program to return the sum and the average of the digits that appear in the string, ignoring all other characters.

import string
st = "12hello wordld12312"
nums = string.digits
print(nums)
val = 0
l = list()
for i in st:
    if i.isdigit():
        val = int(i)
        l.append(val)
    else:
        continue
print(l)
print(sum(l))
print(f"the averageis {sum(l)/len(l)}")