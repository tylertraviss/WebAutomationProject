Feature: Purchasing Clothes

    Background:
        Given I am on the login page
        When I log in with valid credentials
        Then I should see the delete account link
    
    @productsTest
    Scenario: Accessing Product Page
        When I will go to the products page
        Then I will add product id 2
        Then Click continue shopping
        Then I will add product id 3
        Then Click continue shopping
        Then I can see all items I have in my cart
        Then I remove shirt id 1
        #
        Then I proceed to checkout
        Then I place my order
        Then I fill in my credentials
        Then I click to pay