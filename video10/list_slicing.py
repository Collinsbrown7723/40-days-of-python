print("#"*10 + "list slicing"+ "#"*10)
numbers = [1,1,2,34,5,6]
nums  = numbers[1:5]
print(nums)
print(numbers[:])
print(numbers[:3]) #0 as default
print(numbers[5:]) #-1 as default
print(numbers[0:5:2])
print(numbers[4:1:-2])
print(numbers[0:2])
numbers[0:2] = ["a","b","r"]
print(numbers)
print("#"* 10 + "list iteration" + 10 * "#")
l = ["192.168.22.1","192.222.10.1","10.0.0.1"]

for ip in l:
    print(f"connection to {ip}")
print("10.0.0.1" in l) # is in ip T
print("10.0.0.2" in l) # in not in ip F
print("102.0.0.0" is not l) #thats a true statement