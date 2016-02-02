from cart import *
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

