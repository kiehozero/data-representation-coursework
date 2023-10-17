import json

data = {
    'name': 'Joe',
    'age':21,
    'student':True
}

print(data)

filename = "dr2.4-json.json"

with open(filename, "r") as fp:
    jsonobject = json.load(fp)

print(jsonobject)