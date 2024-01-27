import sys
content = "file content"
if len(sys.argv) > 1:
    for x in sys.argv[1:]:
        with open(x,"a") as f:
            f.write(content)
            print(content)
else:
    print("the script reques at least one argument __filename__")