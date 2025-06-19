from collections import defaultdict

class MetroCard:
    def __init__(self, id, balance):
        self.id = id
        self.src = None
        self.balance = balance

    def add_balance(self, amount):
        self.balance += amount

    def update_src(self, src):
        self.src = src

class Station:
    def __init__(self, name):
        self.name = name
        self.total_amount = 0
        self.discount = 0
        self.passengerHistory = defaultdict(int)

    def add_amount(self, x):
        self.total_amount += x

    def add_discount(self, x):
        self.discount += x

    def add_passenger(self, type):
        self.passengerHistory[type] += 1
