#split() and join()

s1 = "h:e who mu:st not named"
l1 = s1.split(" ")
print(l1)

ip = ["192.222.0.1","182.3.3.2","10.0.01"]
new_ip = ",".join(ip)
print(new_ip)