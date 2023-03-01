import requests


r = requests.get("https://api.github.com/repos/Kirit-Singh/BME547_Classwork_Spring2023")
print(r)
print(type(r))
