import json

with open('data.json') as f:
    data = json.load(f)

print(type(data))
for x in data:
    print(x)