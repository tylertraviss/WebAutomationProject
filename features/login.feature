Feature: User Authentication

  Scenario: User can see the logout link after successful login
    Given I am on the login page
    When I log in with valid credentials
    Then I should see the delete account link

  Scenario: User gives the wrong login credentials and is denied access
    Given I am on the login page
    When I write incorrect credentials
    When I press submit
    Then I am prompted with invalid credentials statement

# Also check if are showing error signing in message properly.
# Test the wrong login credentias

