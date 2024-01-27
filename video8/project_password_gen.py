import string
import random
fchars = ""
lengh = ""

chars = string.digits + string.ascii_letters + string.punctuation
lengh = int(input("Enter password lengh:"))
for _ in range(lengh):
    choice = random.choice(chars)
    fchars +=choice
print(f"Your password is {fchars}")
    