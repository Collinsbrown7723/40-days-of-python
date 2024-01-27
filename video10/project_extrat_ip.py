interface = """
wlo1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.100.0.12  netmask 255.255.240.0  broadcast 10.100.15.255
        inet6 fe80::5af5:738b:bd70:3b5c  prefixlen 64  scopeid 0x20<link>
        ether e0:9d:31:7d:f2:2c  txqueuelen 1000  (Ethernet)
        RX packets 1233  bytes 127476 (124.4 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 1258  bytes 304850 (297.7 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

"""

interface_list = interface.splitlines()
#print(interface_list)

ip_mac = list()
for line in interface_list[2:5]:
        temp = line.split()
        ip_mac.append(temp[1])
print(ip_mac)
print(",".join(ip_mac))