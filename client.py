import requests


server = "http://127.0.0.1:5000"


r = requests.get(server + "/info")
print(r.status_code)
print(r.text)


out_data = {"name": "Kirit", "HDL_value": 55}
r = requests.post(server + "/HDL_analysis", json=out_data)
print(r.status_code)
print(r.text)


out_data = {"a": 2, "b": 3}
r = requests.post(server + "/add", json=out_data)
print(r.status_code)
print(r.text)
x = r.json()
print(x + 2)
