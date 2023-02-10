class Patient:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.mrn = 0
        self.age = 0
        self.tests = []

    def get_full_name(self):
        full_name = "{} {}".format(self.first_name,
                                   self.last_name)
        age = 15
        print(age)
        print(self.age)
        return full_name


def main():
    new_patient = Patient()
    second_patient = Patient()
    print(new_patient)
    print(second_patient)
    new_patient.first_name = "Kirit"
    new_patient.last_name = "Singh"
    new_patient.tests.append(("HDL", 100))
    print(new_patient.first_name)
    print(new_patient.last_name)
    print(new_patient.tests)
    print(new_patient.get_full_name())
    print(second_patient.first_name)


if __name__ == "__main__":
    main()
