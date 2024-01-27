"""How to solve this coding challenge:

Write your solution in PyCharm or in your preferred Python IDE and then run the script.

If your solution is not correct, then try to understand the error messages, rewrite the solution and run the Python script again. Repeat this step until you get the correct solution.



Coding Challenge

In order to simply the serialization and deserialization process your task is:

1. Create a function called serialize() that takes 3 arguments: 1) the Python object you want to serialize, 2) the file to which it serializes the object and 3) the serialization protocol which is pickle or json.

The function will create the file (the 2nd argument) and will write the Python object to that file according to its 3rd argument. If the 3rd argument is pickle, It will use pickle to serialize the object and if the argument is json it will use json for serialization.

2. Create a function called deserialize() that takes 2 arguments: 1) the file which contains serialized data and 2) the type of deserialization which is pickle or json.

The function will deserialize from the file into a Python object and will return that object.

3. Test the functions by serializing and deserializing Python objects using both pickle and json.

Note: The script can also be used as a module that will be imported in other Python scripts.

Are you stuck? Do you want to see the solution for this exercise? Click here."""
import json
import pickle


text_file = str(input("Enter the file you want to read:"))
try:
    with open(text_file,"rt")as f:
        text = f.read() 
except Exception as e:
    print(e.args)







def serialize(obj,file_name,protocol):
    if protocol == "json":
        with open(file_name,"w")as f:
            json.dump(obj,f,indent=4)
    elif protocol == "pickle":
        with open(file_name,"wb")as f:
            pickle.dump(obj,f)
    else:
        print("Protocol must be json or pickle.")
        return 0
    
    with open(file_name,"rb") as f:
        if protocol == "json":
            data = json.load(f)
            return data

        elif protocol == "pickle":
            data = pickle.load(f)
            return data
a = serialize(text,"test.json","json")
print(a)