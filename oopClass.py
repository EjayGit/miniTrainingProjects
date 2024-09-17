class StarCookie:
    milk = 0.1
    
    def __init__(self, weight, colour):
        self.weight = weight
        self.colour = colour

starCookie1 = StarCookie(15, 'red')
print(starCookie1.weight)
print(starCookie1.colour)
starCookie2 = StarCookie(16, 'blue')
print(starCookie2.weight)
print(starCookie2.colour)
print(starCookie1.__dict__)
print(StarCookie.__dict__)