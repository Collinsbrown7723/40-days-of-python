while True:
    
    try:
        a = int(input("Enter a:"))
        b = int(input("Enter b:"))
        v = 9
        c = a/b+v
        print(c)
    except ZeroDivisionError as e:
        print(f"Division by 0 is not allowed{e.args}")
    except TypeError as e:
        print(f"canno add ints a strings {e.args}")
    except Exception as e:
        print(f"this a generic exception {e.args}")
    else:
        print("No erros")
        break
    finally:
        print("Good bye")
    print("some other lines of code")

age = -1

if age < 0:
    raise Exception("Age bellow 0 is not accepted")