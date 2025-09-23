import json

data = {
    "name" : "Tejas",
    "age" : 22,
    "marks" : [23,45,76]
}

with open("student.json", "w") as jsonfile:
    json.dump(data, jsonfile)

with open("student.json", "r") as jsonfile:
    data = json.load(jsonfile)
    print(data)