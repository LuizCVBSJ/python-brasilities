import requests
from cep_access import AdressSearch

cep1 = AdressSearch("11685402")
request = "https://viacep.com.br/ws/{}/json".format(cep1)
r = requests.get(request)

print(r)
print(r.text)
