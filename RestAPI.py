import requests
import json

base_url = "https://jsonplaceholder.typicode.com/users"

#Response Object
response = requests.get(base_url)

print(type(response))


#Attribute of the Response Object
if response.status_code == 200: 
    datas = response.json()
    print(type(datas))

print(datas[0])

'''for data in datas:
    if data.get("id") == 1:
        print(data["name"])'''


