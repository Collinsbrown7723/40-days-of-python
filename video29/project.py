import json 
#import requests

# url = "https://jsonplaceholder.typicode.com/todos/"
# data = requests.get(url)
# json_data = data.json()
# #print(json_data)

# with open("todos.json","w") as f:
#     json.dump(json_data,f,indent=4)
    
new_list = list()
with open("todos.json","rt") as f:
    todos = json.load(f)
#print(todos[1]["completed"])  
for x in todos:
    if x["completed"] == True:
        new_list.append(x)
for x in new_list:
    print(x)

