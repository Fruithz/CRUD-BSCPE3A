class Employee:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

class EmployeeFactory:
    @staticmethod
    def create_employee(name, email, phone):
        return Employee(name, email, phone)
