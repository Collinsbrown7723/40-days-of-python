with open("text.txt","w")as f:
    f.write("this is write mode acn create file if no exist\n")

with open("text.txt","a")as f:
    f.write("this the append 'a' mode, can create file not exist\n")

with open("text.txt","r+") as f:
    f.seek(5)
    f.write("100")
    f.write("this append but to the top of the file")