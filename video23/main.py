# Total number of IPv6 (each ipv6 consists of 128 bits)
no_of_ipv6 = 2 ** 128

no_of_digits = len(str(no_of_ipv6))

print(no_of_digits)     # => 39
phone = {'Brand':'Samsung', 'Price':650.2, 'Seller': 'Nile'}
print(dir(phone))
#Adding a new key:value pairs to the dictionary
phone.update({'OS':'Android', 'Color': 'Black'})
phone = {'Brand':'Samsung', 'Price':650.2, 'Seller': 'Nile'}

price = phone['Price']
vat = format(price * 0.19, '.2f')   # format() returns a string
print(type(vat))
vat = float(vat)                    # casting to float

print(vat)      # => 123.54
my_list = [1, 2.3, 'abc', (5, 6, 'x', 'y')]

my_var = str(my_list[1]) + my_list[2][0] + my_list[-1][-1]
print(my_var)       # => 2.3ay
languages = ['English', 'Python', 'Java', 'Golang', 'German']

# Slicing that returns a new list with elements from index 1 included to index -1 excluded
languages = languages[1:-1]
print(languages)        # => ['Python', 'Java', 'Golang']
my_list = list(range(-20, 8, 3))
print(my_list)  # => [-20, -17, -14, -11, -8, -5, -2, 1, 4, 7]
days = [10, 11, 13, 14, 15]

## Inserting 12 at index 2
days.insert(2, 12)

# print(days)     # => [10, 11, 12, 13, 14, 15]
message = 'Wow! Python is great'
vowels = 'aeio'

no_vowels = [x for x in message if x not in vowels and x != " "]

print(no_vowels)   # => ['W', 'w', '!', 'P', 'y', 't', 'h', 'n', 's', 'g', 'r', 't']
names1 = {'John', 'Marry', 'Lena', 'Pollux'}
names2 = {'Dan', 'Arthur', 'Marry', 'Lena', 'Castor'}

# Set Intersection
names = names1 & names2     # names is of type set
names = list(names)         # converting set to list

print(names)    # => ['Lena', 'Marry']
phone1 = ['1111', '2222', '2222', '1111']
phone2 = ['1111', '3333', '3333', '1111']

# Converting lists to sets (to remove duplicates) and using the union operation
# union() or | returns the set of all unique elements present in all the sets.
phone_numbers = set(phone1) | set(phone2)

# Equivalent to:
phone_numbers = set(phone1).union(set(phone2))


print(phone_numbers)    # => {'1111', '3333', '2222'}
my_str  = 'wlo1      Link encap:Ethernet  HWaddr b4:6d:83:77:85:f3'

my_list = my_str.split()
# my_list is ['wlo1', 'Link', 'encap:Ethernet', 'HWaddr', 'b4:6d:83:77:85:f3']


# We concatenate the first list element, '!' and the last list element
interface_mac = my_list[0] + '!' + my_list[-1]
print(interface_mac)    # => wlo1!b4:6d:83:77:85:f3
def my_function(num):
    result = int(num) + int(num*2) + int(num*3)
    return result

result = my_function('5')
print(result)   # => 615
#List with duplicates
mac = ['b4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3', 'a4:6d:83:77:85:f4', 'c4:6d:83:77:85:f3', 'b4:6d:83:77:85:f3']

# New empty list
mac_unique = list()

# Iterate over the list
for item in mac:
    if item not in mac_unique:
        mac_unique.append(item)
  # add it if it's not in the mac_unique list

print(mac_unique)
#List with duplicates
years = [2010, 2010, 2011, 2011, 2012, 2012, 2012]

# New list with unique elements
years_unique = []

# Adding only unique elements from years in years_unique
[years_unique.append(x) for x in years if x not in years_unique]

print(years_unique) # => [2010, 2011, 2012]
#List of Words
words = ['Anna', 'Car', 'Civic', 'Screen', 'Level', 'Cat', 'Mom' ]

# List comprehension that constructs a list of palindromes from names list
palindromes = [ items for items in words if items.lower() == items[::-1].lower() ]

print(palindromes)      # => ['Anna', 'Civic', 'Level', 'Mom']
def reverse(my_str):
    """
    This function returns a new string with all characters reversed.
    """
    return my_str[::-1]     # slicing with a step of -1


output = reverse('Beautiful')
print(output)       # => lufituaeB
def remove_from_list(my_list, item):
    """
    Function that removes an item from a list.
    """
    while item in my_list:
        my_list.remove(item)

list1 = [1, 2, 1, 1, 1, 1, 3]

# Calling the function and remove 1 from the list
remove_from_list(list1, 1)

print(list1)        # => [2, 3]
def vowel_count(my_str):
    """
    This function counts the number of vowels in a string
    """
    vowels = 'aeiou'
    my_str = my_str.lower()
    
    new_dict = dict()
    for x in my_str:
        if x in vowels:
            if x in new_dict.keys():
                new_dict[x] +=1
            else:
                new_dict[x] = 1
    return new_dict        
        
        
r = vowel_count('Awesome')
print(r)    # => {'a': 1, 'e': 2, 'o': 1}


r = vowel_count('Wow! Python is great!')
print(r)    # => {'o': 2, 'i': 1, 'e': 1, 'a': 1}
def counter(my_str):
    vowels = 'aeiou'
    no_of_vowels = 0

    #letter case doesn't matter
    my_str = my_str.lower() # make a lowercase copy of my_str

    for char in vowels:
        no_of_vowels += my_str.count(char)

    no_of_consonants = len(my_str) - no_of_vowels

    return (no_of_vowels, no_of_consonants)


print(counter('Python'))  # => (1, 5)
print(counter('BeautifUl'))  # => (5, 4)
s1 = "collins"

print(s1.count("l"))

# Assigning the lambda expression to a variable called area
# length is the lambda argument
area = lambda x: x **2
print(area(2))
# The value of the constant PI with many decimal points
PI = 3.141592653589793

PI = format(PI,".5f") #format returns a string
PI = float(PI)
print(PI)
countries = {'us': 'United States of America', 'br': 'Brazil', 'de': 'Germany', 'at': 'Austria'}

# List of keys sorted in alphabetical order
keys = sorted(countries.keys())

# Iterate over the keys and print the corresponding value of the dictionary
for k in keys:
    print(countries[k])
salaries = {'John': 50000, 'Anne': 66000, 'Antonio': 48000}

taxes = {k:v *0.1 for k,v in salaries.items()} 
print(taxes)    # => {'John': 5000.0, 'Anne': 6600.0, 'Antonio': 4800.0}
# Opening the file in read only mode
f = open('a.txt', 'r')

# Move the cursor on position 4 inside the file
f.seek(4)

# Read 5 characters starting with position 4 and return them in variable called word
word = f.read(5)
print(word)    # => first

# Closing the file
f.close()
# Opening the file in append mode
with open('workout.txt', 'a') as file:
    file.write('May 25:8800\n')  # appending to the end of the file