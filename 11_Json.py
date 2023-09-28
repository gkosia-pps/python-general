# %%
import json
from typing import Any

person_json = """{ \
 "name": "gab"
,"age": 33
,"fav": ["boxing", "volleyball"]
} \
"""

person_dict = { 
 "name": "gab"
,"age": 33
,"fav": ["boxing", "volleyball"]
}


# %%
# dict to string
print(json.dumps(person_dict,indent=4,sort_keys=True))

# %%
# write json to file
# dumps used to convert to string, dump is used to write it to a stream
with open('person.json', 'w') as file:
    json.dump(person_dict,file,indent=4)

# %%
# json string to python dict, loads used to load from string
person = json.loads(person_json)
print(person)

# %%
# read json from file, load is used to read from source
with open('person.json', 'r') as file:
    person = json.load(file)
    print(person)
# %%
# Serialize objects to dump them using a custom encode function
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def encodeUser(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object is not serializable")
    
u1 = User("gab", 33)

userjson_enc = json.dumps(u1, default=encodeUser)
print(userjson_enc)

# %%
# Serialize objects to dump them creating a custom encode class

from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        return JSONEncoder.default(self,o)
    
# userEncodedstring = json.dumps(u1,cls=UserEncoder)
# or
userEncodedstring = UserEncoder().encode(u1)
print(userEncodedstring)
# %%
# Decode json to python objects
user = json.loads(userEncodedstring)
print(type(user))

def decodeUser(dct):
    if User.__name__ in dct:
        return User(name =dct["name"], age = dct["age"])

u = json.loads(userEncodedstring, object_hook=decodeUser)
print(u.name, u.age)

# %%
