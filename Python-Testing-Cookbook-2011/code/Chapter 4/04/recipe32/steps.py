from lettuce import *
from cart import *

@step("an empty cart")
def an_empty_cart(step):
    world.cart = ShoppingCart()

@step("looking up the fifth item causes an error")
def looking_up_fifth_item(step):
    try:
        world.cart.item(5)
        raise AssertionError("Expected IndexError")
    except IndexError, e:
        pass

@step("looking up a negative price causes an error")
def looking_up_negative_price(step):
    try:
        world.cart.price(-2)
        raise AssertionError("Expected IndexError")
    except IndexError, e:
        pass

@step("the price with no taxes is (.*)")
def price_with_no_taxes(step, total):
    assert world.cart.total(0.0) == float(total)

@step("the price with taxes is (.*)")
def price_with_taxes(step, total):
    assert world.cart.total(10.0) == float(total)

@step("I add a carton of milk for (.*)")
def add_a_carton_of_milk(step, price):
    world.cart.add("carton of milk", float(price))

@step("I add another carton of milk for (.*)")
def add_another_carton_of_milk(step, price):
    world.cart.add("carton of milk", float(price))

@step("the first item is a carton of milk")
def check_first_item(step):
    assert world.cart.item(1) == "carton of milk"

@step("the price is (.*)")
def check_first_price(step, price):
    assert world.cart.price(1) == float(price)

@step("the cart has (.*) items")
def check_size_of_cart(step, num_items):
    assert len(world.cart) == float(num_items)

@step("the total cost with (.*)% taxes is (.*)")
def check_total_cost(step, tax_rate, total):
    assert world.cart.total(float(tax_rate)) == float(total)

@step("I add a carton of milk")
def add_a_carton_of_milk(step):
    world.cart.add("carton of milk", 2.50)

@step("I add a frozen pizza")
def add_a_frozen_pizza(step):
    world.cart.add("frozen pizza", 3.00)

@step("the second item is a frozen pizza")
def check_the_second_item(step):
    assert world.cart.item(2) == "frozen pizza"

@step("the first price is (.*)")
def check_the_first_price(step, price):
    assert world.cart.price(1) == float(price)

@step("the second price is (.*)")
def check_the_second_price(step, price):
    assert world.cart.price(2) == float(price)

@step("the total cost with no taxes is (.*)")
def check_total_cost_with_no_taxes(step, total):
    assert world.cart.total(0.0) == float(total)

@step("the total cost with (.*)% taxes is (.*)")
def check_total_cost_with_taxes(step, tax_rate, total):
    assert round(world.cart.total(float(tax_rate)),2) == \
                                              float(total)
