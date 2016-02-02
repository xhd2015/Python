from cart41 import *

class recipe41:
    def __init__(self):
        self.cart = None

    def create_empty_cart(self):
        self.cart = ShoppingCart()

    def lookup_item(self, index):
        try:
            return self.cart.item(int(index))
        except IndexError:
            return "ERROR"

    def lookup_price(self, index):
        try:
            return format(self.cart.price(int(index)), ".2f")
        except IndexError:
            return "ERROR"

    def add_item(self, description, price):
        self.cart.add(description, float(price))

    def size_of_cart(self):
        return len(self.cart)

    def total(self, tax):
        return format(self.cart.total(float(tax)), ".2f")

    def store_cart(self):
        return self.cart.store()

    def retrieve_cart(self, id):
        self.cart.retrieve(id)

    def size_of_cart(self):
        return len(self.cart)
