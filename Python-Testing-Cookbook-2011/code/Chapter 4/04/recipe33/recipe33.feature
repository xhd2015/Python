Feature: Shopping cart
  As a shopper
  I want to load up items in my cart
  So that I can check out and pay for them

    Scenario: Empty cart
      Given an empty cart
      Then looking up the fifth item causes an error
      And looking up a negative price causes an error
      And the price with no taxes is 0.0
      And the price with taxes is 0.0

    Scenario: Cart getting loaded with multiple of the same
      Given an empty cart
      When I add a carton of milk for 2.50
      And I add another carton of milk for 2.50
      Then the first item is a carton of milk
      And the price is 5.00
      And the cart has 2 items
      And the total cost with 10% taxes is 5.50

    Scenario: Cart getting loaded with different items
      Given an empty cart
      When I add a carton of milk
      And I add a frozen pizza
      Then the first item is a carton of milk
      And the second item is a frozen pizza
      And the first price is 2.50
      And the second price is 3.00
      And the total cost with no taxes is 5.50
      And the total cost with 10% taxes is 6.05
