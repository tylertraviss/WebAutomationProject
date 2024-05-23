# from selenium.webdriver.common.by import By
# from base_page import BasePage

# class CartPage(BasePage):
#     CART_ITEM = (By.CLASS_NAME, "cart_item")
#     REMOVE_BUTTON = (By.CLASS_NAME, "remove")

#     def get_cart_product_count(self):
#         return len(self.driver.find_elements(*self.CART_ITEM))

#     def remove_product(self, product_index):
#         cart_items = self.driver.find_elements(*self.CART_ITEM)
#         if product_index < len(cart_items):
#             remove_button = cart_items[product_index].find_element(*self.REMOVE_BUTTON)
#             remove_button.click()
#         else:
#             raise IndexError(f"Product with index {product_index} not found")

#     def proceed_to_checkout(self):
#         checkout_button = self.find_element(By.LINK_TEXT, "Proceed to Checkout")
#         checkout_button.click()
