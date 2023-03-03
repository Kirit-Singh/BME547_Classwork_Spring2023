import requests


server = "http://vcm-7631.vm.duke.edu:5002"

patient_IDs = requests.get(server + "/get_patients/ks625")
print(patient_IDs.text)


p1_type = requests.get(server + "/get_blood_type/F8")
print(p1_type.text)


p2_type = requests.get(server + "/get_blood_type/F3")
print(p2_type.text)


out_data = {"Name": "ks625", "Match": "No"}
blood_match = requests.post(server + "/match_check", json=out_data)
print(blood_match.status_code)
print(blood_match.text)
