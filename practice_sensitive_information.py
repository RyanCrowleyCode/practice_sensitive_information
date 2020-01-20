# Practice: Sensitive Information
# Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization

# Social security number
# Date of birth
# Health insurance account number
# First name
# Last name
# Address

class Patient():
    def __init__(self, ssn, dob, hin, first_name, last_name, address):
        self.__ssn = ssn
        self.__dob = dob
        self.__hin = hin
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address

    @property
    def ssn(self):
        return self.__ssn

    @property
    def dob(self):
        return self.__dob

    @property
    def hin(self):
        return self.__hin

    @property
    def full_name(self):
        return f'{self.__first_name} {self.__last_name}'

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, new_address):
        self.__address = new_address



# The first three properties should be read-only. First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name. Address should have a getter and setter.

jim = Patient("123-45-6789", "09/30/2000", "7001294103", "Jim", "Jones", "123 Street Blvd")

print(jim.full_name)
jim.address = "90210 Felicia Blvd"


