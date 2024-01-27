#Write a Python program that displays the multiplication table (from 1 to 10) of a specific integer number entered by the user.

value = int(input("Enter number: "))
count = 1
for _ in range(0,10):
    print(f"{value} X {count} = {value*count}")


#or 
value = int(input("Enter number: "))
count = 1
for _ in range(1,11):
    print(f"{value} X {count} = {value*_}")