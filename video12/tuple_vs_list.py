# tuple as faster and more efficient list
# we save tuple to store contants
#tuple are safer than list // bug free
#tuples can be used a keys in dictionaries
# store efficiently
import sys
l1 = [2,3,4]
t1 = (2,4,5)
print(f"memory size for list{sys.getsizeof(l1)}")
print(f"memory size for tuple{sys.getsizeof(t1)}")