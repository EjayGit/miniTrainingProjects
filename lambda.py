squared = lambda num: num**2
print(squared(5))

add = lambda a, y: a+y
print(add(2, 3))

multiply = lambda a, b, c: a*b*c
print(multiply(1,2,3))

power = lambda x, y: x**y
print(power(2, 3))

power = lambda x, y=2: x**y
print(power(4))
print(power(5,3))

myList = [2, 4, 3, 5, 8, 5, 3, 7]
myList.sort()
print(myList)

names = ['Even Park', 'Edy Lucky', 'Kelly Adams', 'Smith Baker']
print(names)
names.sort(key=lambda x: x.split()[1])
print(names)

people = [('Evan', 20),('Edy', 19),('Kelly', 30),('Smith', 25)]
people.sort(key=lambda x: x[1])
print(people)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name}:{self.age}'

Evan = Person('Evan', 20)
Edy = Person('Edy', 19)
Kelly = Person('Kelly', 30)

persons = [Evan, Edy, Kelly]
print(persons)
persons.sort(key=lambda x: x.name)
print(persons)