import requests
import json

base = "https://jsonplaceholder.typicode.com/users"

#Response Object
response = requests.get(base)

print(type(response))

#Attribute of the Response Object
if response.status_code == 200: 
    datas = response.json()
    print(type(datas))

for x in datas:
    print()
    for key, Value in x.items():
        print(f"Key: {key}, Value: {Value}")

'''for data in datas:
    if data.get("id") == 1:
        print(data["name"])'''


