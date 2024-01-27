alphabets = dict()
# with open("video14/phonetic-alphabet.csv","r") as c:
#     #alphabets.update(c)
#     for C in c.readlines():
#         alphabets[C[0]] = C[2:]
#         print(C[0],C[2:])

# word = input("Enter your word: ")
# for _ in word:
#     print(alphabets[_.capitalize()])
with open("video14/phonetic-alphabet.csv","r") as c:
    words = c.read().splitlines()
    for item in words[1:]:
        letter, word = item.split(",")
        alphabets[letter] = word 
    print(alphabets)    
    
my_str = "abcd".upper()
print(my_str ,end = " => ")
for char in my_str:
    print(alphabets[char], end="    ")  