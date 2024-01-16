import json


def readjson(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        print(json.dumps(data, indent=4))
filename = "exercici23.json"
readjson(filename)