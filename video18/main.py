


new_list = list()
with open("devices.txt","r") as f:
    content = f.read().splitlines()
    for l in content[1:]:
        new_list.append(l.split(":"))
print(new_list[1][0])
for ip in new_list:
    print(f" pinging {ip[1]}")