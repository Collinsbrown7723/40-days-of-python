#Write a Python program to check if an integer (x) is the power of another integer (y). Prompt the user to input both integers.

st = "hello world"
vs = "aeoiu"
l =list()

for _ in range(0,len(st)):
    if st[_] in vs:
        print(st[_])
        l.append(st[_])
    else:
        continue
print(l)
print(len(l))

vowels = 'aeiou'
my_str = 'Cogito, ergo sum.'

count = 0
for v in vowels:
    if v in my_str.lower():
        count += my_str.count(v)

print(f'Total number of vowels: {count}')
        