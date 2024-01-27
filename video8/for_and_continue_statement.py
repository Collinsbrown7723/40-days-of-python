for letter in "hello python world":
    if "o" in letter: #each time the python sees o it will skipp it
        continue
    print(letter,end="") 
#                      hell pythn wrld

for n in range(10):
    if n % 2 == 0:
        print(f"found an even number{n}")
        continue
    print(f"found an odd number{n}")
for _ in range(1000000):
    pass