import json


def create_person():
	new_person = {"First Name": "Anna",
	              "Last Name": "Ables",
	              "Age": 35,
	              "Visits": ["1/1/2020", "2/3/2020", "3/15/2020"]   
	              }
	return new_person


if __name__=="__main__":
    person = create_person()
    print(person)