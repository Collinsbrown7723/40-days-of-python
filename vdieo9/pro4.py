# Write a Python script that checks if a triangle is equilateral, isosceles or scalene.
# The user will be prompted for the triangle sides.
# Note:
# An equilateral triangle is a triangle in which all three sides have the same length.
# An isosceles triangle is a triangle that has two equal sides.
# A scalene triangle is a triangle that has three unequal sides.
# Input: Enter the lengths of the triangle sides:
# x: 6
# y: 8
# z: 12

x = int(input("Enter value for x"))
y = int(input("Enter value for y"))
z = int(input("Enter value for z"))

if x == y and x == z and y == z:
    print(f"{x,y,z}is an equileteral")
elif x == y or x == z or y == z:
    print(f"{x,y,z} is an isosceles")
else:
    print(f"{x,y,z}is scalene")
        