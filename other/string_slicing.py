# slicing_varialble[start:stop]
movie = "Harry Potter"
print(movie[0:2])# output = 'Ha'
print(movie[:]) # this return all the string literal
print(movie[::-1]) #this return the string literal but in revers
print(movie[-2:]) #er
print(movie[:4]+movie[4:])#movie[:i] + movie[i:] = the whole string 
print(movie[:67]) #out of range slice indexs are managed without errors
#slices also accept a third value 'step'  when not specified the default is set to 1
# slicing_varialble[start:stop:step]
print(movie[:10:2])