f = open("a.txt","r") 
try:
    f.read()
except:
    print("can not read file")
else:
    print("file read succesfully")
finally:
    if not f.closed:
        f.close()
    print("bye")
    