#1 f.read().splitlines()
with open("configuration.txt","rt")as f:
    content = f.read().splitlines()
    print(content)
#2 f.readlines()
print("#"*70)
with open("configuration.txt","rt")as f:
    print(f.readline(), end="")
    print(f.readline())
    
#3 list(f)
with open("configuration.txt","rt")as f:
    print(list(f))

#iteration

with open("configuration.txt","rt")as f:
    for line in f:
        print(f.read(),end="")
    