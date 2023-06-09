
   
  

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
inventory = Inventory()
inventory.add_to_inventory("banana", 10)
inventory.add_to_inventory("apples", 5)
inventory.add_to_inventory("carrots", 20)
inventory.add_to_inventory("spinach", 40)
inventory.add_to_inventory("cabbage", 75)
inventory.add_to_inventory("onions", 70)
inventory.add_to_inventory("lemons", 90)
inventory.add_to_inventory("watermelon", 15)
inventory.add_to_inventory("oranges", 50)

# adding items to the cart
inventory.add_to_cart("banana", 2)
inventory.add_to_cart("apples", 4)
inventory.add_to_cart("carrots", 10)
inventory.add_to_cart("cabbages", 5)
inventory.add_to_cart("spinach", 2)
inventory.add_to_cart("lemons", 4)
inventory.add_to_cart("garlic", 10)
inventory.add_to_cart("mangoes", 5)

#Update  the inventory
inventory.add_to_inventory("cucumbers", 5)
inventory.add_to_inventory("sukuma wiki", 10)
inventory.add_to_inventory("onions", 5)
inventory.add_to_inventory("brocolli", 10)
inventory.add_to_inventory("apples", 5)
inventory.add_to_inventory("strawberries", 10)
inventory.add_to_inventory("carrots", 5)
inventory.add_to_inventory("pineapples", 10)
inventory.add_to_inventory("dodo", 5)
inventory.add_to_inventory("lemons", 10)



