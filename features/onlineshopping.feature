Feature: Online Shopping Testing

    Background:
        Given I am on the login page
        When I log in with valid credentials
        Then I should see the delete account link
    
    @productsTest
    Scenario: Accessing Product Page
        When I will go to the products page
        Then I will add product id 2
        Then Click continue shopping