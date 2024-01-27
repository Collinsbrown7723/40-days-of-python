f = open("./configuration.txt")
print(f.read(5))
print(f.read(5))
print(f.read(5))
print(f.tell())
f.seek(2)
print(f.read(3))
f.close()#save resource