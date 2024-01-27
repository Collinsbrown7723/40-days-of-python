#lambda parameter_list : expression
def add(a,b,c):
    result = a+b+c
    return result
result = (lambda a,b,c:a+b+c)(2,3,5)
print(result)

square = lambda x = 10: x**2
print(square(2))
print(square())

friend = [("collinsssssssss",23),("yohanan",45),("achman",100)]
friend.sort() 
print(friend) 
#to sort by age

friend.sort(key= lambda x: x[1])
print(friend)
friend.sort(key= lambda x:len(x[0]))
print(friend)