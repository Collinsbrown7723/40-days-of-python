def format_ipv4_address_count(count):
    if count >= 1e9:
        return f"{count / 1e9:.1f} billion"
    elif count >= 1e6:
        return f"{count / 1e6:.1f} million"
    elif count >= 1e3:
        return f"{count / 1e3:.1f} thousand"
    else:
        return str(count)

allip = 2 ** 32
classA = 2 ** 8
classB = 2 ** 16
first = format_ipv4_address_count(allip)
second = format_ipv4_address_count(classA)
third = format_ipv4_address_count(classB)
print(f'this is all the addresses {first}')
print(f'this the class A number{second}')
print(f'this the class B number{second}')

