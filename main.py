import requests

def httpbin_get():
	return requests.get('http://httpbin.org/get')

if __name__ == '__main__':
	r = httpbin_get()
	print(r.json())