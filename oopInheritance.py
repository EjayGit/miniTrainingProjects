class Person:

    def __init__(self, name, phoneNumber, address):
        self.phoneNumber = '0'
        self.name = name
        self.address = address

    def update_contact(self, new_number):
        self.phoneNumber = new_number
        print(f"The updated number is {self.phoneNumber}")

class Customer(Person):
    def __init__(self, name):
        super().__init__(name=name, phoneNumber='', address='')

    def purchase(self, item):
        print(f"{item} has been purchased.")

newPerson = Person(name='Erik', phoneNumber=0, address='here')
print(newPerson.phoneNumber)
newCustomer = Customer('James')
newCustomer.purchase('Coffee')
print(newCustomer.phoneNumber)
newCustomer.update_contact('222-323-2222')
print(newCustomer.phoneNumber)