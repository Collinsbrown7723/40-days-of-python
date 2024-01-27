def is_perfect_number(n):
    """
    Check if a number is a perfect number.
    
    Parameters:
    - n (int): The number to check.
    
    Returns:
    - bool: True if the number is perfect, False otherwise.
    """
    # Find all divisors (excluding the number itself)
    divisors = [x for x in range(1, n) if n % x == 0]

    # Sum the divisors
    divisor_sum = sum(divisors)

    # Check if the sum of divisors equals the original number
    return divisor_sum == n


"""Challenge #3

Write a function that returns the factorial of a number n which is the function's argument."""
def factorail(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * factorail(n - 1)


result = factorail(5)
print(result)


def fact(n):
    if n < 0:
        print('The function\'s argument (n) should be greater than or equal to zero.')
    elif n == 0:
        return 1
    else:
        f = 1
        while n > 0:
            f *= n
            n -= 1
        return f


print(fact(10))
print(80 * "#")


"""Challenge #4

Create a function that takes an integer as an argument and returns True if its a prime number and False otherwise.

"""

def is_prime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True
print(is_prime(2))
print(is_prime(89))

print(70 * "#")
"""Challenge #5

Using the function defined in the previous challenge find 5 prime numbers greater than 1,000,000"""
for x in range(1_000_000,1_000_100):
    if is_prime(x):
        print(x)
        
        
"""Challenge #6

Write a function called fibo that takes an integer greater than 10 as an argument and returns the Fibonacci series between 0 and the function's argument."""
"""0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers before it:

"""
num1 = 0
num2 = 1
l1 = list()
for i in range(10):
    print(num1,num2)
    tmp = num1 + num2
    l1.append(tmp)
    num1 , num2 = num2, tmp
    
print(l1)
# n = 100
# a, b = 0, 1
# while a <= n:
#     print(a, ' ', end=' ')
#     a, b = b, a + b