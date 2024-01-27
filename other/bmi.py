ht = 0
wt = 0
ht = float(input("Enter your height: "))
wt = float(input("Enter your weight: "))

bmi = wt/ht**2
print(f"your BMI value is {format(bmi,'.2f')}")