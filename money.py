class Money:
    def __init__(self, amount):
        self.amount = amount

    def add_money(self, amount):
        self.amount += amount

    def sub_money(self, amount):
        self.amount -= amount