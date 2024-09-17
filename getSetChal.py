class Employee:
    
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    #def __getSalary(self):
    #    return self.__salary

    #def __setSalary(self, newSalary):
    #    self.__salary = newSalary

    #salary = property(__getSalary, __setSalary)

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, newSalary):
        self.__salary = newSalary

employee1 = Employee('Erik', 1000)
employee2 = Employee('Alex', 1500)
print(employee1.name)
print(employee1.salary)
employee1.salary = 1200
print(employee1.salary)
#print(employee1.getSalary())       # __get etc
#print(employee1.setSalary(1500))   # __set etc
#print(employee1.getSalary())       # __get etc
print(employee2.salary)
employee2.salary = 1700
print(employee2.salary)