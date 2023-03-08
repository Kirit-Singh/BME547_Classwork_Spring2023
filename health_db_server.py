"""
Database = Dictionary
keys -> ids for the patients
value: int

{1: {"id": 1, "name": "Kirit", "blood_type": "B+"},
 2: {"id"}
"""


from flask import Flask, request, jsonify


db = {}


app = Flask(__name__)


def add_patient_to_db(id, name, blood_type):
    new_patient = {"id": id,
                   "name": name,
                   "blood_type": blood_type}
    db[id] = new_patient


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    # Get input data
    in_data = request.get_json()
    new_patient_driver(in_data)
    return jsonify(answer)
    # Call other functions to do the work
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    # Return a response


def new_patient_driver(in_data):
    # Validate input
    validation = validate_input_data(in_data)
    if validation is not true:
        return validation, 400
    # Do the work
    # Return an answer


def validate_input_data(in_data):
    if type(in_data) is not dict:
        return "Input is not a dictionary"
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    for key, value_type in zip(expected_keys, expected_types):
        if key not in in_data:
            return "Key {} is missing from input".format(key)
        if type(in_data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True
