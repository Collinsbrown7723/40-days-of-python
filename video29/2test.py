"""How to solve this coding challenge:

Write your solution in PyCharm or in your preferred Python IDE and then run the script.

If your solution is not correct, then try to understand the error messages, rewrite the
solution and run the Python script again. Repeat this step until you get the correct solution.



Coding Challenge

1. Using requests connect to https://jsonplaceholder.typicode.com/users and take the JSON
 encoded string in Python object


2. The resulting Python object will be a list of dictionaries. Process the list and extract 
the following information for each user:

- Name

- City

- GPS coordinates in form of (LAT, LNG)

- Company's name the user is working for

3. Write to a CSV File a row for each user. The fields of t
he CSV file will be: name, city, GPS coordinates and company's name


For example for the first user you'll write in the CSV file
: Leanne Graham,Gwenborough,"(-37.3159,81.1496)",Romaguera-Crona


Are you stuck? Do you want to see the solution for this exe
rcise? Click here."""

url = "https://jsonplaceholder.typicode.com/users"
import requests

# data = requests.get(url)
import json
import csv
# d = data.json()
# with open("users.json","w") as f:
#     json.dump(d,f,indent=4)
    
with open("users.json","rt") as f:
    obj = json.load(f)
    for x in obj:
        name = x["name"]
        city = x["address"]["city"]
        gps = x["address"]["geo"]
        company = x["company"]["name"]
        print(name,gps,company)
        new_ls = [name,city,gps,company]
        with open("users.csv","a+") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow(new_ls)