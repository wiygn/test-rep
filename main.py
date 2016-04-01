import requests

r = requests.get('http://httpbin.org/get?kek=foo')

print(r.json())