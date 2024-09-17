import requests
import json


base_url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(base_url)

if response.status_code == 200: 
    datas = response.json()

for data in datas:
    if data.get("id") == 1:
        print(data["name"])

mitsos = "Nikos"
for x in mitsos:
    print(x, end="")