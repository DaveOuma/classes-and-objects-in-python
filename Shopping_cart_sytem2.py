class Product:
    def __init__(self, name, price, description, image, category):
        self.name = name
        self.price = price
        self.description = description
        self.image = image
        self.category = category

class Shopping_Cart:
    def __init__(self):
        self.items = []
        self.discounts = []
        
    def add_item(self, product, quantity=1):
        for item in self.items:
            if item.product.name == product.name:
                item.quantity += quantity
                return
        self.items.append(CartItem(product, quantity))
    
    def remove_item(self, product, quantity=1):
        for item in self.items:
            if item.product.name == product.name:
                if item.quantity >= quantity:
                    item.quantity -= quantity
                    if item.quantity == 0:
                        self.items.remove(item)
                else:
                    print(f"Insufficient quantity of {product.name} in cart.")
                return
    
    def empty_cart(self):
        self.items = []
        self.discounts = []
        
    def get_total(self):
        total = 0
        for item in self.items:
            total += item.product.price * item.quantity
        for discount in self.discounts:
            total -= discount.amount
        return total
    
    def display_cart(self):
        print("** Shopping Cart **")
        for item in self.items:
            print(f"{item.quantity}x {item.product.name} - ${item.product.price:.2f} ({item.product.category})")
            print(f"{item.product.description}")
            print(f"Image: {item.product.image}")
        print(f"Total: ${self.get_total():.2f}")
        
    def add_discount(self, type, amount):
        """
        type: "item" or "total"
        amount: percentage (for "item") or fixed amount (for "total")
        """
        self.discounts.append(Discount(type, amount))

    def checkout(self):
        if self.items:
            print("** Checkout **")
            self.display_cart()
            # Simulate payment processing (can be replaced with actual payment integration)
            print("Payment processed successfully.")
            self.empty_cart()
        else:
            print("Your cart is empty. Please add items to proceed.")


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Discount:
    def __init__(self, type, amount):
        self.type = type
        self.amount = amount


# Creating products
apple = Product("Apple", 0.50, "Fresh and juicy red apple.", "apple.jpg", "Fruits")
banana = Product("Banana", 0.75, "Perfect for a healthy snack.", "banana.jpg", "Fruits")
milk = Product("Milk", 2.99, "Whole milk for your daily calcium.", "milk.jpg", "Dairy")

# Creating a shopping cart
cart = Shopping_Cart()

# Adding items to the cart
cart.add_item(apple, 2)
cart.add_item(banana, 3)
cart.add_item(milk)  # Adds 1 by default

# Displaying the cart before removing
cart.display_cart()

# Removing items from the cart
cart.remove_item(banana, 2)  # Remove 2 bananas
cart.remove_item(apple, 3)  # Attempt to remove more than available

# Displaying the cart after removing
cart.display_cart()

# Emptying the cart
cart.empty_cart()

# Displaying the empty cart
cart.display_cart()

# Checking out
cart.checkout()
