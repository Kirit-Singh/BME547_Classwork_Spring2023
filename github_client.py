import requests


r = requests.get("https://api.github.com/repos/Kirit-Singh/BME547_CLasswork_Spring2023/branches")
print(r)
print(type(r))
