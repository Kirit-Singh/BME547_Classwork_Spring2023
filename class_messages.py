import requests


send_message = {"user": "ks625", "message": "Hello!"}
r1 = requests.post("http://vcm-21170.vm.duke.edu:"
                   "5001/add_message", json=send_message)
r2 = requests.get("http://vcm-21170.vm.duke.edu:"
                  "5000/get_messages/ks625")
print(r2.text)
