friends = {'collins': [20, 'ghana'], 'mark': [30, 'ghana']}
import json

with open("friens.json","w") as f:
    json.dump(friends,f,indent = 4)
#to load jsom to a variable string use the dumps function

json_string = json.dumps(friends)
print(json_string)
