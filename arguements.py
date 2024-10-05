def multiply(*args):
    print(args)
    result = 1
    for i in args:
        result *= i
    return result

print(multiply(1,2,3,4,5))

def total(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key,value)
    print(kwargs["b"])

def power(n, **kwargs):
    power = 1
    sm = 0
    for i in range(n):
        power *= kwargs["a"]
        sm += kwargs["b"]
    return power, sm

total(a=1, b=2)
print(power(5, a=5, b=2))

class Phone:
    def __init__ (self, **kw):
        self.make = kw.get("make") # 'get' gets if possible
        self.model = kw.get("model")

myPhone = Phone(make="Apple")

print(myPhone.make)
