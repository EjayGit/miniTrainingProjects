# TODO 1 - Create Bike Rental Class and initialize stock attribute
class BikeRental:
    def __init__(self, stock):
        self.stock=stock

# TODO 2 - Create a method to display stock
    def displayStock(self):
        print(self.stock)

# TODO 3 - Create a method to rent bike on hourly bases
    def hourRent(self, num):
        if self.stock<num:
            print(f"There are only {self.stock} bikes left.")
        else:
            self.stock = self.stock - num
            print(f"Please take your bikes.")

# TODO 4 - Create a method to rent bike on daily bases


# TODO 5 - Create a method to rent bike on weekly bases


# TODO 6 - Create a method to return bike from the system


# TODO 7 - Create Customer Class and initialize attributes


# TODO 8 - Create a method to request bike from the system


# TODO 9 - Create a method to return bike to the system


# TODO 10 - Main program logic : print options to the console


# TODO 11 - Ask from user to get option (check if it is int)


# TODO 12 - Based on selected choice call methods from Bike
