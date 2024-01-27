for number in range(10):
    print(number)
    if number == 5:
        break #break statement exits the process
    
for letter in "python":
    if letter == "o":
        print("break out of loop found 'o'")
        break #the break statement prunes the code
    print(letter)
for number in range(1,10):
    if number % 13 ==0:
        print(f"there is a number divicible by 30 in this range{number}")
        break
else:#this else belong to the for loop
    print("no Divisions found")

for i in "abc":
    print(i)
    for n in range(3):
        if n == 1:
            break
        print(n)
