# most commondly use mood are read write append
# "r" read mode
# "rb" read a binary file
# "rt" read in text mode
f = open("configuration.txt","rt")
f.close()
print(f.closed)