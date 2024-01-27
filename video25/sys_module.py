import sys

if sys.platform == "linux":
    print("specifc setting and commands for linux")
elif sys.platform == "mac":
    print("specifc setting and commands for mac")
elif sys.platform == "win32":
    print("specifc setting and commands for windows")
sys.path

l1 = list(range(10000))
s1 = set(l1)
t1 = tuple(l1)
sys.getsizeof(l1)
sys.getsizeof(s1)
sys.getsizeof(t1)

