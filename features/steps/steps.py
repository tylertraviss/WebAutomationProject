from behave import given, when, then
import logging
from selenium import webdriver
from pages.login_page import LoginPage
import time, os
#from pages.products_page import ProductsPage
#from pages.cart_page import CartPage
#from pages.checkout_page import CheckoutPage
from selenium.webdriver.common.by import By

# Create the 'allLogs' folder if it doesn't exist
log_folder = 'allLogs'
if not os.path.exists(log_folder):
    os.makedirs(log_folder)

# Define log format
log_format = '%(asctime)s - %(levelname)s - %(message)s'

# Dynamically generate log file name using current time
current_time = time.strftime("%Y-%m-%d_%H-%M-%S")
log_file = os.path.join(log_folder, f'WebAutomationProject_{current_time}.log')

logging.basicConfig(filename=log_file, level=logging.INFO)
logger = logging.getLogger(__name__)

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Edge()  # Initialize WebDriver (replace with appropriate browser)
    context.login_page = LoginPage(context.driver)
    context.login_page.load()

    logger.info('Arrived on login page.')
    

@when('I log in with valid credentials')
def step_impl(context):
    email = "ttravis@qac.com"
    password = "QAPassword"
    context.login_page.login(email, password)
    logger.info('Attempting to login with credentials username: {}, and password: {}'.format(email, password))

# @then('I should see the products page')
# def step_impl(context):
#     assert '/products' in context.driver.current_url, "Expected to be on the products page, but not found"
#     context.driver.quit()  # Close the browser

@then('I should see the delete account link')
def step_impl(context):
    delete_account_link_locator = (By.XPATH, "//a[contains(text(), 'Delete Account')]")
    delete_account_link = context.driver.find_elements(*delete_account_link_locator)
    assert delete_account_link, "Delete Account link not found on the page, not successfully logged in."
    logger.info('I can see the delete account link, thus I am logged in.')

    context.driver.quit()  # Close the browser

# @given('I can add 2 T-Shirts I like to cart')
# def step_impl(context):
#     context.driver = webdriver.Edge()  # Initialize WebDriver (replace with appropriate browser)
#     context.login_page = LoginPage(context.driver)
#     context.login_page.load()

# @given('I am on the products page')
# def step_impl(context):
#     context.driver = webdriver.Edge()
#     context.products_page = ProductsPage(context.driver)

# @when('I add 2 T-Shirts to the cart')
# def step_impl(context):
#     context.products_page.add_product_to_cart(2)
#     context.products_page.continue_shopping()
#     context.products_page.add_product_to_cart(3)
#     context.products_page.view_cart()

# @when('I view the cart')
# def step_impl(context):
#     context.cart_page = CartPage(context.driver)

# @then('I should see 2 products in the cart')
# def step_impl(context):
#     assert context.cart_page.get_cart_product_count() == 2

# @when('I remove 1 T-Shirt from the cart')
# def step_impl(context):
#     context.cart_page.remove_product(2)

# @then('I should see 1 product in the cart')
# def step_impl(context):
#     assert context.cart_page.get_cart_product_count() == 1

# @when('I proceed to checkout')
# def step_impl(context):
#     context.cart_page.proceed_to_checkout()

# @when('I enter my card details and place the order')
# def step_impl(context):
#     context.checkout_page = CheckoutPage(context.driver)
#     context.checkout_page.enter_card_details()
#     context.checkout_page.place_order()

# @then('I should be able to download an invoice')
# def step_impl(context):
#     assert context.checkout_page.download_invoice()
#     context.driver.quit()