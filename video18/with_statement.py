with open("configuration.txt","rt") as f:
    content = f.read()
    print(content)
print(f.closed)