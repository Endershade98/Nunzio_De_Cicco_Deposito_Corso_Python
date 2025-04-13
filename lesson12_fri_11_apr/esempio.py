import json 
import requests


filjson = '{"name": "Nunzio","surname": "De Cicco"}'
_dict = json.loads(filjson) # convertitto
print(_dict["name"])

my_dict = {"name": "Nunzio","surname": "De Cicco"}
_my_dict = json.dumps(my_dict)
print(type(my_dict)) # convertito
print(_my_dict["name"])



url = "https://open-meteo.com/en/docs?current=temperature_2m"
response = requests.get(url)
_dict = json.loads(response)
#print(_dict[])

# elemento JSON:
x_ = '{"name":"John", "age":30, "city":"New York"}'
# leggi x:
y = json.loads(x_)
# il risultato è un dizionario Python quindi per avere il valore basta scrivere:
print(y["age"])

# dizionario python:
x = { "name": "John",
"age": 30,
"city": "New York"}
# conversione in JSON:
y = json.dumps(x)
# risultato stringa
print(y)


response = requests.get("https://www.google.it")
#response = requests.request("GET", "https://www.google.it)
print(response.json())


response = requests.get("https://www.google.it")
#response = requests.request("GET", "https://www.google.it)
Response_text=response.text()
Response_json = json.loads(Response_text)