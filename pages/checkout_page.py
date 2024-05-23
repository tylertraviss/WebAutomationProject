# from selenium.webdriver.common.by import By
# from base_page import BasePage

# class CheckoutPage(BasePage):
#     CARD_NUMBER_INPUT = (By.ID, "card_number")
#     PLACE_ORDER_BUTTON = (By.ID, "place_order")
#     DOWNLOAD_INVOICE_LINK = (By.LINK_TEXT, "Download Invoice")

#     def enter_card_details(self):
#         card_number_input = self.find_element(*self.CARD_NUMBER_INPUT)
#         card_number_input.send_keys("4111111111111111")

#     def place_order(self):
#         place_order_button = self.find_element(*self.PLACE_ORDER_BUTTON)
#         place_order_button.click()

#     def download_invoice(self):
#         download_invoice_link = self.find_element(*self.DOWNLOAD_INVOICE_LINK)
#         download_invoice_link.click()
#         return True 
