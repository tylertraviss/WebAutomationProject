from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    LOGIN_URL = "https://www.automationexercise.com/login"
    
    USERNAME_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")

    def load(self):
        self.driver.get(self.LOGIN_URL)

    def login(self, username, password):
        self.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.click_element(*self.LOGIN_BUTTON)
