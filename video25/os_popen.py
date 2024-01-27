import os

output = os.popen("ls -a")
print(output.read())