# def myFuction(**kwargs):
#     print(kwargs)
    
#     for k,v in kwargs.items():
#         print(f"the value for k { k} the value for v { v}")
# myFuction(name="collins",alive=True)
# person = {"name":"me","age":23, "alive":True}
# myFuction(**person)

def connect(ip,port,username,location):
    print(ip,port,username,location)
linux_server = {"ip":"192.222.10.20","port":22,"username":"admin","location":"Ghana"}

connect(**linux_server)
