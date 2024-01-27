"""Challenge #1

Write a Python function that takes a list as an argument and returns a new list with unique elements of the first list in the same order.

Sample List : [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]

Unique List : [1, 2, 3, 4, 5]"""
l1 = [1,2,3,3,3,3,4,5, 1, 3, 5, 5, 5]
def un_list(x):
    l = set(x)
    return list(l)
print(un_list(l1))


"""Challenge #2

Write a Python function to check whether a number is perfect or not. The function 
should return True if the number is perfect and False otherwise.

Perfect numbers: https://www.britannica.com/science/perfect-number"""
def all_divisors(n):
    """
     This function returns all divisors of a number
    """
    divisors = []
    for x in range(1, int(n/2)+1):
        if n % x == 0:
            divisors.append(x)
    return divisors


def perfect_number(n):
    divs = all_divisors(n)
    if sum(divs) == n:
        return True
    else:
        return False


# calling the function
n = 496
if perfect_number(n):
    print(f'{n} is one rare of a kind number, it\'s a perfect number')
else:
    print(f'Nothing special about {n}, it\'s no perfect number')


"""Challenge #3

Write a function that returns the factorial of a number n which is the function's argument.

Factorial: https://en.wikipedia.org/wiki/Factorial

"""

def factorail(n):
    """find the factorial of a number n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorail(n - 1) 
result = factorail(20)
print(result)

"""Challenge #4

Create a function that takes an integer as an argument and 
returns True if its a prime number and False otherwise.

Are you stuck? Do you want to see the solution to this exercise? Click here."""





def is_prime(n):
    prime = True
    if n == 1: # 1 is not a prime number, the first prime numnber is 2
        return False
    i = 1
    while i < n // 2:
        i = i + 1
        if n % i == 0:
            prime = False
            break
    return prime # returns True or False


            
            
"""Challenge #5

Using the function defined in the previous challenge find 5 prime numbers greater than 1,000,000

Are you stuck? Do you want to see the solution to this exercise? Click here."""



""""
Challenge #6

Write a function called fibo that takes an integer greater than 10 as an argument and returns the Fibonacci series between 0 and the function's argument.

Fibonacci Series: https://www.mathsisfun.com/numbers/fibonacci-sequence.html

Example: fibo(23) will return 0, 1, 1, 2, 3, 5, 8, 13, 21"""


"""Challenge #7

Write a function that takes a list as an argument and returns the Equilibrium Index of the list. If there isn't such an index it returns False.

Equilibrium index: https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

Are you stuck? Do you want to see the solution to this exercise? Click here.

"""



"""Challenge #8

Change the solution of the previous challenge so that the function receives a string of numbers separated by a comma.

Example:

nums = '2, 3, 10, 5'

print(equilibrium_index(nums)) # => 2

nums = '3, 3, 10, 5'

print(equilibrium_index(nums)) # => False"""




"""Challenge #9

Define a function that draws a Christmas tree using asterisks (*). The function takes a single argument, which is the height of the tree.

Example: by calling draw_tree(5) it will display:

*

***

*****

*******

*********"""