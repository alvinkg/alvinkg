# how to parse json into py dict

from collections import UserDict
import json


# sample json here
userJSON = '{"first_name": "John", "last_name": "Doe", "age": 30}'

# parse to dict
user = json.loads(userJSON)
print(user)
print(user['first_name'])

# dump dict to json
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1870}
carJSON = json.dumps(car)
print(carJSON)
