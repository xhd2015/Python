from lettuce import *
from should_dsl import should, should_not
from cart import *

@step("an empty cart")
def an_empty_cart(step):
    world.cart = ShoppingCart()

@step("looking up the fifth item causes an error")
def looking_up_fifth_item(step):
    (world.cart.item, 5) |should| throw(IndexError)

@step("looking up a negative price causes an error")
def looking_up_negative_price(step):
    (world.cart.price, -2) |should| throw(IndexError)

@step("the price with no taxes is (.*)")
def price_with_no_taxes(step, total):
    world.cart.total(0.0) |should| equal_to(float(total))

@step("the price with taxes is (.*)")
def price_with_taxes(step, total):
    world.cart.total(10.0) |should| equal_to(float(total))

@step("I add a carton of milk for 2.50")
def add_a_carton_of_milk(step):
    world.cart.add("carton of milk", 2.50)

@step("I add another carton of milk for 2.50")
def add_another_carton_of_milk(step):
    world.cart.add("carton of milk", 2.50)

@step("the first item is a carton of milk")
def check_first_item(step):
    world.cart.item(1) |should| equal_to("carton of milk")

@step("the price is 5.00")
def check_first_price(step):
    world.cart.price(1) |should| equal_to(5.0)

@step("the cart has 2 items")
def check_size_of_cart(step):
    len(world.cart) |should| equal_to(2)

@step("the total cost with 10% taxes is 5.50")
def check_total_cost(step):
    world.cart.total(10.0) |should| equal_to(5.5)

@step("I add a carton of milk")
def add_a_carton_of_milk(step):
    world.cart.add("carton of milk", 2.50)

@step("I add a frozen pizza")
def add_a_frozen_pizza(step):
    world.cart.add("frozen pizza", 3.00)

@step("the second item is a frozen pizza")
def check_the_second_item(step):
    world.cart.item(2) |should| equal_to("frozen pizza")

@step("the first price is 2.50")
def check_the_first_price(step):
    world.cart.price(1) |should| equal_to(2.5)

@step("the second price is 3.00")
def check_the_second_price(step):
    world.cart.price(2) |should| equal_to(3.0)

@step("the total cost with no taxes is 5.50")
def check_total_cost_with_no_taxes(step):
    world.cart.total(0.0) |should| equal_to(5.5)

@step("the total cost with 10% taxes is (.*)")
def check_total_cost_with_taxes(step, total):
    world.cart.total(10.0) |should| close_to(float(total), \
                                            delta=0.1)
