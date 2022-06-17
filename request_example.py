import requests

endpoint = 'http://127.0.0.1:5000/pegarvendas'

req = requests.get(endpoint) # request to endpoint

res = req.json()

print(req)
print(req.json())
print(res['total_vendas'])