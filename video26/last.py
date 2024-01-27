from functools import wraps

# defining a decorator
def timer(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        stop = time.time()
        print(f"{func.__name__} took {start - stop} to finish" )
        return result
    return wrapper


# decorating the function
@timer
def sum_of_powers(n, p):
    nums = [x ** p for x in range(1, n)]
    return sum(nums)


s = sum_of_powers(1000000, 2)
print(s)

s = sum_of_powers(1000000, 3)
print(s)

s = sum_of_powers(1000000, 5)
print(s)

## EXPECTED OUTPUT:

# sum_of_powers execution time:0.33020472526550293
# 333332833333500000
# sum_of_powers execution time:0.33238673210144043
# 249999500000250000000000
# sum_of_powers execution time:0.36234617233276367
# 166666166667083333333333250000000000