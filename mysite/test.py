import requests

url_11 = 'http://127.0.0.1:8000'
url_12 = 'http://127.0.0.1:8000'
url_21 = 'http://127.0.0.1:8000/api'
url_22 = 'http://127.0.0.1:8000/api?method=ping'
url_23 = 'http://127.0.0.1:8000/api?method=home'

print(requests.get(url_11))
print(requests.post(url_12))

print(requests.get(url_21))
req = requests.post(url_22)
print(req, req.text)
print(requests.post(url_23))



