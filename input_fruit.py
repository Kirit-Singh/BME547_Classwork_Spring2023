def analyze_ID(input_line):
    patient_data = first_line.strip("/n").split("=")
    patient_id = int(patient_data[1])
    return patient_id


def read_file():
    in_file = open(filename, "r")
    first_line = in_file.readline()
    id = analyze_ID(first_line)


def test_read_file():
    from module import read_file
    filename = "my_test_data.txt"
    answer = read_file(filename)
    expected = 50
    assert == expected
