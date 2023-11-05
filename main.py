import requests
from cep_access import AdressSearch

cep1 = AdressSearch("11696036")

print(cep1)

r = requests.get("https://viacep.com.br/ws/01001000/json")

print(r)
print(type(r))
