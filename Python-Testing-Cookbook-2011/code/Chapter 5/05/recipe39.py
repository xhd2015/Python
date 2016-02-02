from cart import *

class recipe39:
    def __init__(self):
        self.cart = ShoppingCart()

    def add_item_to_cart(self, description, price):
        self.cart.add(description, float(price))

    def get_total(self, tax):
        return format(self.cart.total(float(tax)), ".2f")
