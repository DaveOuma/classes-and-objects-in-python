class ShoppingCart:
    def __init__(self):
        self.items = {}  # Initialize an empty dictionary to store items

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity  # If item already exists, increment quantity
        else:
            self.items[item_name] = quantity  # If item doesn't exist, add it with specified quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] > quantity:  # If quantity to remove is less than existing quantity
                self.items[item_name] -= quantity
            else:
                del self.items[item_name]  # If quantity to remove is greater or equal, remove the item completely

    def display_items(self):
        print("Shopping Cart:")
        for item, quantity in self.items.items():
            print(f"- {item}: {quantity}")

# Create objects (instances) of the ShoppingCart class
cart1 = ShoppingCart()
cart2 = ShoppingCart()

# Use the objects to add items
cart1.add_item("Apple", 5)
cart1.add_item("Banana", 3)
cart2.add_item("Milk", 2)

# Display items in each cart
cart1.display_items()
cart2.display_items()

# Remove items from cart1
cart1.remove_item("Apple", 2)
cart1.remove_item("Banana", 5)

# Display updated items in cart1
cart1.display_items()

# Try removing more items than available in cart1
cart1.remove_item("Apple", 5)

# Display updated items in cart1
cart1.display_items()

