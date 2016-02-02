class ShoppingCart(object):
    def __init__(self):
        self.items = []

    def add(self, item, price):
        self.items.append(Item(item, price))
        return self

    def item(self, index):
        return self.items[index-1].item

    def price(self, index):
        return self.items[index-1].price

    def total(self, sales_tax):
        sum_price = sum([item.price for item in self.items])
        return sum_price*(1.0 + sales_tax/100.0)

    def __len__(self):
        return len(self.items)

class Item(object):
    def __init__(self, item, price):
        self.item = item
        self.price = price

import unittest

class ShoppingCartTest(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart().add("tuna sandwich", 15.00)

    def test_length(self):
        self.assertEquals(1, len(self.cart))

    def test_item(self):
        self.assertEquals("tuna sandwich", self.cart.item(1))

    def test_price(self):
        self.assertEquals(15.00, self.cart.price(1))

    def test_total_with_sales_tax(self):
        self.assertAlmostEquals(16.39, \
                                self.cart.total(9.25), 2)

