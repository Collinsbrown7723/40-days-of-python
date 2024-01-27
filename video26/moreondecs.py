#################################
## Decorators - The @ Syntax
#################################
import functools
file_to_del = input("enter the name of the file you want delete: ")
users_name = input("what is your usename? ")
roll = input("what is your roll, only admins can delet files : ")
user = dict()
user["level"] = str(roll)
user["username"] = str(users_name)
print(user.items())

# defining a decorator
def only_admin(func): # decorators wrap a function, modifying its behavior.
    @functools.wraps(func)
    def wrapper_only_admin(*args, **kwargs):
        """this function check user previlages"""
        if user['level'] == 'admin' and user["username"] == "root":
            return func(*args, *kwargs)
        else:
            raise PermissionError("You have no permission to remove the file!")

    return wrapper_only_admin


@only_admin   # @ or pie syntax
def remove_file(f = None):
    """
    It removes a file.
    """
    import os, os.path
    if os.path.isfile(file_to_del):
        os.remove(file_to_del)
        print(f'{file_to_del} removed!')
    else:
        print('Argument is not file!')

print(remove_file.__doc__)
print(remove_file.__name__)


try:
    remove_file('a.txt')
except PermissionError as e:
    print(e)

# equivalent to following code and without @only_admin before remove_file() definition:
# try:
#     remove_file = only_admin(remove_file)
#     remove_file('a.txt')
# except PermissionError as e:
#     print(e)

