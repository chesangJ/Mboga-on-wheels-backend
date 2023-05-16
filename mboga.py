class Stock:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
    def add_stock(self, quantity):
        self.quantity += quantity
    def remove_stock(self, quantity):
        if self.quantity >= quantity:
            self.quantity -= quantity
        else:
            print(f"Not enough {self.name} in stock")