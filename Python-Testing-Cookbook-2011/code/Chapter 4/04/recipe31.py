import unittest
from copy import deepcopy
from recipe31_cart import *
from mockito import *

class CartThatWeWillSaveAndRestoreUsingMockito(unittest.TestCase):
    def test_fill_up_a_cart_then_save_it_and_restore_it(self):
        # Create an empty shopping cart
        cart = ShoppingCart(DataAccess())

        # Add a couple of items
        cart.add("carton of milk", 2.50)
        cart.add("frozen pizza", 3.00)

        self.assertEquals(2, len(cart))

        # Create a clone of the cart for mocking
        # purposes.
        original_cart = deepcopy(cart)

        # Save the cart at this point in time into a database
        # using a mock
        cart.storer = mock()

        when(cart.storer).store_cart(cart).thenReturn(1)
        when(cart.storer).retrieve_cart(1). \
                               thenReturn(original_cart)

        id = cart.store()

        self.assertEquals(1, id)

        # Add more items to cart
        cart.add("cookie dough", 1.75)
        cart.add("ginger ale", 3.25)

        self.assertEquals(4, len(cart))

        # Restore the cart to the last point in time
        cart.restore(id)

        self.assertEquals(2, len(cart))

        verify(cart.storer).store_cart(cart)
        verify(cart.storer).retrieve_cart(1) 
    
