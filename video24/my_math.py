

a = 10

def my_sum(*args):
    s = 0
    for number in args:
        s = s + number
    return s
if __name__ =="__main__":
    print(f"__name__ in math.py {__name__}")