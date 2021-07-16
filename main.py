# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import requests
import json

url="https://randomuser.me/api"

response=requests.get(url)
print(response.text)

jsonDataString= response.text
jsonDictionary= json.loads(jsonDataString)
persona=jsonDictionary["results"][0]
nombre=persona["name"]["first"]+" "+persona["name"]["last"]
correo=persona["email"]
print(nombre, correo, sep=",")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
