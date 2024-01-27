#the continue statement returns the control back to the beging of the while loop
x = 12

while x < 100:
    x += 1
    if x % 13 !=0:
        continue #when x is div by 13 the print statement will run
    print(x) 