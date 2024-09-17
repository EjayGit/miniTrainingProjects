class Person:
    def __init__(self, name, phone, address, email):
        self.name = name
        self.phone=phone
        self.address=address
        self.email=email

    def update_contact(self, phone, address):
        self.phone=phone
        self.address=address
        print(f"The contact details have been updated to {self.phone} {self.address}")

class Employee(Person):
    def __init__(self, name, employee_number):
        super().__init__(name=name)
        self.employee_number=employee_number

    def promote(self):
        print(f"{self.name} has been promoted!")

    def retire(self):
        print(f"{self.name} has been retured!")

class Customer(Person):
    def __init__(self, name, customerID):
        super().__init__(name=name)
        self.customerID=customerID

    def purchase():
        pass

class Courier(Person):
    def __init__(self, name):
        super().__init__(name=name)

    def deliver_packages(self):
        print(f"The package has been delivered by {self.name}")

newEmployee