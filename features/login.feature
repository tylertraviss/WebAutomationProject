Feature: User Authentication

  Scenario: User can see the logout link after successful login
    Given I am on the login page
    When I log in with valid credentials
    Then I should see the delete account link

# Also check if are showing error signing in message properly.
# Test the wrong login credentias

# Feature: Online Shopping

#   Scenario: Purchase T-Shirts and Download Invoice
#     Given I can add 2 T-Shirts I like to cart
#     And I can see all products I have added in the cart
#     And I am able to remove 1 T-Shirt that I don't like from the cart
#     When I am ready to buy
#     And I proceed to checkout and place my order
#     And I enter my card details and pay for the order
#     Then I am able to download an Invoice
