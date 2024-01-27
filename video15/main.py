# """Challenge #1

# Create a Python script that removes all the elements of a list that are duplicates.

# Do the challenge in a single line of code using sets."""
# l1 = [2,2,3,4,5,2,3,4]
# l1 = set(l1)
# print(l1,type(l1))
# print(list(l1))

# """Consider a list of words (strings). Write a Python script that generates a dictionary where the key is the word in the list and the value is its length.

# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

# Expected Result: {'Python': 6, 'Java': 4, 'C++': 3, 'Golang': 6, 'Solidity': 8, 'Bash': 4}

# """
# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# new_dict = dict()
# for c in words[:]:
#     print(c)
#     new_dict[c] = len(c)
# print(new_dict)

# """Challenge #3

# Considering the following dict, get a dict representation sorted by key.

# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

# A dict representation means viewing or printing the dict.

# """
# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# dk = d1.keys()
# dv = d1.values()
# sorted(d1)
# print(dk,dv)

# """Challenge #4

# Considering the following dict, get a dict representation sorted by value.

# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

# A dict representation means viewing or printing the dict.
# Challenge #5

# Let's generalize the last challenge and sort a dictionary by any field of its values if the value is a composite type (list, tuple, etc).

# Example: Considering this dictionary print a sorted view of the dictionary by the second field of its values.

# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# The output should be: [('Diana', ('NYC', 3500, 31)), ('Maria', ('Zagreb', 3800, 40)), ('John', ('London', 4000, 28))]

# P.S. Do it with a single line of code."""
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# print(type(employees))
# list_employees = list(employees.items())
# print(list_employees[::-1])

# """Challenge #6 xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Consider this dictionary. Print a sorted view of the dictionary by the third field of its values, in reverse order.

# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# The output should be: [('Maria', ('Zagreb', 3800, 40)), ('Diana', ('NYC', 3500, 31)), ('John', ('London', 4000, 28))]

# P.S. Do it with a single line of code.

# """
# print(30* "#")
# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# print(employees)
# print([list(l[::-1]) for l in employees.items()])
# """Challenge #7

# Consider the dictionary called COUNTRY declared in this Python script.

# The keys are the country codes and the values are the country names.

# Print a sorted view of the dictionary, by the key (country code)."""
# country = {233:"Ghana",234:"Nigeria",123:"USA"}
# print(country[233])



# """Challenge #9

# Consider the following two Python Lists that save information about company sales for the last 6 years:

# years = [2015, 2016, 2017, 2018, 2019, 2020]

# sales = [350000, 400000, 410000, 439000, 500000, 290000]

# Create a new list that connects the year to the corresponding sales.

# The resulting list should be: [(2015, 350000), (2016, 400000), (2017, 410000), (2018, 439000), (2019, 500000), (2020, 290000)]

# """
# years = [2015, 2016, 2017, 2018, 2019, 2020]

# sales = [350000, 400000, 410000, 439000, 500000, 290000]
# z = zip(years,sales)
# neww_dict = dict()
# neww_dict.update(z)
# print(list(neww_dict.items()))

# """Consider the following two Python Lists that save information about company sales for the last 6 years:

# years = [2015, 2016, 2017, 2018, 2019, 2020]

# sales = [350000, 400000, 410000, 439000, 500000, 290000]

# Create a new dictionary that has the keys, the years, and the values, the sales.

# The resulting dict should be: {2015: 350000, 2016: 400000, 2017: 410000, 2018: 439000, 2019: 500000, 2020: 290000}"""
# years = [2015, 2016, 2017, 2018, 2019, 2020]

# sales = [350000, 400000, 410000, 439000, 500000, 290000]
# z = zip(years,sales)
# company = dict()
# company.update(z)
# key = company.keys()
# vals = company.values()
# l1 = list(company.items())
# print(l1,type(l1))
# new_dict = dict()
# for k,v in l1:
#     print(k,v)
#     new_dict[k]=v
# print(new_dict)

# """Challenge #11

# Consider the dictionary from the previous challenge.

# Create a new dictionary called profit that stores the profit of the company, if the profit margin is 25% of the sales.

# Use dictionary comprehension if possible.

# """
# profit = list()

# l2 = list(new_dict.items())
# print(l2)
# for v in l2[:]:
#     profit.append(v[1])
# print(sum(profit))

# """Challenge #12

# Consider the following 2 Lists: names = ["Dan", "John", "Diana"] and phones = [11111, 2222, 3333].

# Create a set that contains the elements of the 2 lists in pairs.

# The resulting set should be: {('John', 2222), ('Diana', 3333), ('Dan', 11111)}

# """
# names = ["Dan", "John", "Diana"]
# phones = [11111, 2222, 3333]

# l1 = list()

# z = zip(names,phones)
# d1 = dict()
# d1.update(z)
# s1 = set(d1.items())
# l1 = [tuple(s)[::-1] for s in s1]
# print((l1))

"""Challenge #14

Write a Python script that validates an email address by writing "Valid email!" or "Invalid email!".

If the email is not valid the script should display why it's not valid.

We consider a valid email address if:

it has at least 6 characters but no more than 16.

it contains both . and @

it does not contain any of the following characters:'[]{}()$*'

"""
mail = input("Enter your email: ")
bol = "@" in mail
is_correct_email = False
if len(mail) >= 6+8:
    print("pass1")
    if  bol == True:
        print("pass2")
        is_correct_email = True
if is_correct_email == True:
    print("your email is valid")
elif is_correct_email == False:
    print("your email is invalid try adding more\n letters and the @ simbole")