import subprocess

try:
    with open("a.txt","r") as f:
        ip = f.readlines()
    print(ip)
except Exception as e:
    print(e.args)




count = 0
while count < len(ip):
    for _ in ip:
        host = _
        count +=1
        print(host)
        command = f"ping -c 1 {host}"
        try:
            output  = subprocess.check_output(command.split())
            print(output.decode())
        except Exception as e:
            print(e.args)
        else:
            print("succes")
        finally:
            print("i run regarlles")