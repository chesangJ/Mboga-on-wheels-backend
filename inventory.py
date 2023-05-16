class Inventory:
    def __init__(self):
        self.items = {}
    def add_to_inventory(self, name, quantity):
        if name in self.items:
            self.items[name].add_stock(quantity)
        else:
            self.items[name] = Stock(name, quantity)
    def add_to_cart(self, name, quantity):
        if name in self.items:
            self.items[name].remove_stock(quantity)
            print(f"{quantity} {name} added to cart")
            print(f"Remaining stock for {name}: {self.items[name].quantity}")
            
        else:
            print(f"{name} not found in inventory")
