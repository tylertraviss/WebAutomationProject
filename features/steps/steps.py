from behave import given, when, then
import logging
from selenium import webdriver
from pages.login_page import LoginPage
import time, os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

productsButtonPath = 'a[href="/products"]'

@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Edge()  # Initialize WebDriver (replace with appropriate browser)
    context.login_page = LoginPage(context.driver)
    context.login_page.load()
    context.driver.maximize_window()
    logger.info('Arrived on login page.')
    

@when('I log in with valid credentials')
def step_impl(context):
    email = "ttravis@qac.com"
    password = "QAPassword"
    context.login_page.login(email, password)
    logger.info('Attempting to login with credentials username: {}, and password: {}'.format(email, password))

@when('I write incorrect credentials')
def step_impl(context):
    logger.info("Fake Email Test")
    email = "fakeemail1234@gmail.com"
    password = "Thispasswordisntreal"
    context.login_page.login(email, password)
    logger.info('Attempting to login with credentials username: {}, and password: {}'.format(email, password))

@when("I press submit")
def step_impl(context):

    # Wait for the login button to be clickable
    login_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="login-button"]'))
    )

    # Click the login button
    login_button.click()


@then("I am prompted with invalid credentials statement")
def step_impl(context):
    error_message_element = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//p[@style="color: red;"][contains(text(), "Your email or password is incorrect!")]'))
    )


@then('I should see the delete account link')
def step_impl(context):
    delete_account_link_locator = (By.XPATH, "//a[contains(text(), 'Delete Account')]")
    delete_account_link = context.driver.find_elements(*delete_account_link_locator)
    assert delete_account_link, "Delete Account link not found on the page, not successfully logged in."
    logger.info('I can see the delete account link, thus I am logged in.')

    #context.driver.quit()  # Close the browser




# -----------------------------------------------------------------------------------------------------------


@when("I will go to the products page")
def step_impl(context):
    context.driver.get("https://www.automationexercise.com/products")
    

@then("I will add product id 2")
def step_impl(context):
    try:
    # Wait until the element is present and clickable
        add_to_cart_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-product-id="2"].add-to-cart'))
        )
        # Click the "Add to cart" button
        add_to_cart_button.click()
        print("Clicked on the 'Add to cart' button.")
        logger.info("Clicked on the 'Add to cart' button for item 1.")
    except Exception as e:
        print(f"An error occurred: {e}")

@then("I will add product id 3")
def step_impl(context):
    try:
    # Wait until the element is present and clickable
        add_to_cart_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[data-product-id="3"].add-to-cart'))
        )
        # Click the "Add to cart" button
        add_to_cart_button.click()
        print("Clicked on the 'Add to cart' button.")
        logger.info("Clicked on the 'Add to cart' button for item 3.")
    except Exception as e:
        print(f"An error occurred: {e}")


@then("Click continue shopping")
def step_impl(context):
     # Wait until the "Continue Shopping" button in the modal is present and clickable
    continue_shopping_button = WebDriverWait(context.driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-success.close-modal.btn-block[data-dismiss="modal"]'))
    )   
    
    continue_shopping_button.click()
    logger.info("Clicked on the 'Continue Shopping' button.") 

@then("I can see all items I have in my cart")
def step_impl(context):
    URL = "https://www.automationexercise.com/view_cart"
    context.driver.get(URL)

@then("I remove shirt id 1")
def step_impl(context):
    # Wait until the element is present and clickable
    delete_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.cart_quantity_delete[data-product-id="2"]'))
    )
    # Click the delete button
    delete_button.click()

@then("I proceed to checkout")
def step_impl(context):
    checkout_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'check_out'))
    )
    # Click the checkout button
    checkout_button.click()

@then("I place my order")
def step_impl(context):
    place_order_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@href="/payment"][@class="btn btn-default check_out"]'))
    )
    # Click the place order button
    place_order_button.click()

@then("I fill in my credentials")
def step_impl(context):
    nameOnCard = "QA Consultants"
    cardNumber = "1234 5678 9101 1123"
    CVC = "123"
    M = "12"
    Y = "2030"

    name_on_card_input = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-qa="name-on-card"]'))
        )
    name_on_card_input.clear()
    name_on_card_input.send_keys(nameOnCard)

    card_number_input = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-qa="card-number"]'))
        )
    card_number_input.clear()
    card_number_input.send_keys(cardNumber)

    cvc_input = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-qa="cvc"]'))
        )
    
    cvc_input.clear()
    cvc_input.send_keys(CVC)

    expiration_month_input = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-qa="expiry-month"]'))
        )
    
    expiration_month_input.clear()
    expiration_month_input.send_keys(M)

    expiration_year_input = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[data-qa="expiry-year"]'))
        )
    
    expiration_year_input.clear()
    expiration_year_input.send_keys(Y)

@then("I click to pay")
def step_impl(context):
    pay_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-qa="pay-button"]'))
        )
    pay_button.click()