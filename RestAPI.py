import requests

base_url = "https://jsonplaceholder.typicode.com/users"

<<<<<<< HEAD
#Response Object
response = requests.get(base_url)

print(type(response))
#Attribute of the Response Object

if response.status_code == 200: 
    datas = response.json()

for data in datas:
    if data.get("id") == 1:
        print(data["name"])


mitsos = "Nikos"
for x in mitsos:
    print(x, end="")
