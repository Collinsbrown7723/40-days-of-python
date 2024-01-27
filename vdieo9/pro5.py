#Write a Python program that calculates and displays the sum, the product and the average of n float numbers entered by the user, each on a separate line. Enter 0 to finish.

#value = int(input("Enter range:"))
sam = 0.0
product = 1
i = 0
count  = 0
while (value :=float(input("Enter the fist number"))) !=0:
    sam += value
    product *= value
    count += 1
print(f"the sum is{sam} and the product is{product}")