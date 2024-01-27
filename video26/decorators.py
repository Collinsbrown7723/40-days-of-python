#@decorators

user = {"username":"collins","level":"admin"}

def has_permission(func):
    def wrapper():
        if user["level"] == "admin":
            return func()
        else:
            return None
    return wrapper

def secret_password():
    return "12345"
    


val = has_permission(secret_password)
s = val()
print(s)

