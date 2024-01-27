s1 = [10,30,49,37,3]
s2 = list()

for _ in s1:
    s2.append(_*2)
print(s2)
s3 = [_*2 for _ in s1]
print(s3)

name = "voldermold"
l4 = [char for char in name]
print(l4)

l5 = [(char*2).upper() for char in name]
print(l5)

frds = ["collins","mark","jnr","pablo"]

l6 = [(item.capitalize()) for item in frds]
print(l6)

reversed_names = [item[::-1] for item in frds]
print(reversed_names)

nums = [2,7,8,14,3,7]
divisible_by_seven = [n for n in nums if n%7==0]
print(divisible_by_seven)
num_str = [str(n) for n in nums if n > 5]
print(num_str)
print("-".join(num_str))
#print("-".join(num)) this is an erro because the .join takes only str
friend = ['collins','Mark','elvis',"Harry","potter"]
iswiz = ['mark','john','harry','potter',"elvis"]
friend_lower = [(n.lower() for n in friend)]
iswiz_lower = [(n.lower() for n in iswiz)]
friend_iswiz = [(name.capitalize()) for name in iswiz_lower  if name in friend_lower]
print(friend_iswiz)