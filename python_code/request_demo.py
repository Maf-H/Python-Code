import requests

r = requests.get("http://localhost:3000/")
if r.status_code == requests.codes.ok:
    print("Successful connection")
    print(r.headers['Content-Type'])

